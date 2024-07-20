from typing import List
from reviews_management.domain.entities.enum.general_review import GeneralReview
from reviews_management.domain.entities.valoration import Valoration
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt


def GetTimeSerieProfile(valorations: List[Valoration], prediction_days: int):
    if prediction_days > 30: 
        prediction_days = 30
    elif prediction_days < 1:
        prediction_days = 1
    
    # Convertir los datos en un DataFrame
    data = [(v.createdAt.date(), v.general_review) for v in valorations]
    df = pd.DataFrame(data, columns=['Date', 'Review'])
    df['Value'] = df['Review'].map({
        GeneralReview.VERY_NEGATIVE: 1,
        GeneralReview.NEGATIVE: 2,
        GeneralReview.NEUTRAL: 3,
        GeneralReview.POSITIVE: 4,
        GeneralReview.VERY_POSITIVE: 5
    })
    
    daily_avg = df.groupby('Date')['Value'].mean().reset_index()
    daily_avg = daily_avg.sort_values('Date')
    
    model = ExponentialSmoothing(daily_avg['Value'], trend='add').fit()
    
    forecast = model.forecast(prediction_days)
    
    x_data = daily_avg['Date'].tolist()
    y_data = daily_avg['Value'].tolist()
    
    last_date = daily_avg['Date'].iloc[-1]
    x_pred = [(last_date + pd.Timedelta(days=day + 1)).strftime('%Y-%m-%d') for day in range(prediction_days)]
    y_pred = forecast.tolist()
    
    # Convertir fechas a cadenas de texto
    x_data = [date.strftime('%Y-%m-%d') for date in x_data]
    
    plt.figure(figsize=(10, 6))
    plt.plot(daily_avg['Date'], daily_avg['Value'], marker='o', linestyle='-', label='Actual')
    future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=prediction_days)
    plt.plot(future_dates, forecast, marker='x', linestyle='--', color='red', label='Forecast')
    plt.title('Daily Average Valoration with Forecast')
    plt.xlabel('Date')
    plt.ylabel('Average Valoration')
    plt.grid(True)
    plt.legend()
    plt.savefig('daily_average_valoration_with_forecast.png')
    plt.close()
    
    return {'x': x_data, 'y': y_data, 'x_pred': x_pred, 'y_pred': y_pred}
