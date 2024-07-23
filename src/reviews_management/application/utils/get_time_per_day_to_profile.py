import io
from typing import List, Dict, Any
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

from publication_management.infraestructure.services.S3_upload_image import S3Service
from reviews_management.domain.entities.enum.general_review import GeneralReview
from reviews_management.domain.entities.valoration import Valoration

async def GetTimeSerieProfile(uuid: str, valorations: List[Valoration], prediction_days: int) -> Dict[str, Any]:
	try:
		if prediction_days > 30: 
			prediction_days = 30
		elif prediction_days < 1:
			prediction_days = 1
			
		if valorations is None or len(valorations) == 0:
			return {'success': False, 'message': "No cuentas con suficientes valoraciones para hacer un pronóstico."}
		
		# Convertir los datos en un DataFrame
		data = [(v.createdAt.date(), v.general_review) for v in valorations]
		df = pd.DataFrame(data, columns=['Date', 'Review'])
		
		if df['Date'].nunique() <= 1:
			return {'success': False, 'message': 'datos insuficientes'}

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
		
		buffer = io.BytesIO()
		plt.figure(figsize=(10, 6))
		plt.plot(daily_avg['Date'], daily_avg['Value'], marker='o', linestyle='-', label='Actual')
		future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=prediction_days)
		plt.plot(future_dates, forecast, marker='x', linestyle='--', color='red', label='Forecast')
		plt.title('Daily Average Valoration with Forecast')
		plt.xlabel('Date')
		plt.ylabel('Average Valoration')
		plt.grid(True)
		plt.legend()
		plt.savefig(buffer, format='png')
		plt.close()
		
		buffer.seek(0)
		
		s3_service = S3Service()
		file_name = f'daily_average_valoration_with_forecast_{uuid}.png'
		mime_type = 'image/png'
		s3_url = await s3_service.execute(buffer.read(), file_name, mime_type)
		
		return {'success': True, 'x': x_data, 'y': y_data, 'x_pred': x_pred, 'y_pred': y_pred, 's3_url': s3_url}
	
	except Exception as e:
		print(e)
		return {'success': False, 'message': "Error, algo salio mal con el pronóstico."}