from reviews_management.domain.entities.enum.general_review import GeneralReview
from transformers import pipeline


def analysis_comment(comment: str):
    modelo = "nlptown/bert-base-multilingual-uncased-sentiment"
    analizador_sentimientos = pipeline("sentiment-analysis",model=modelo)
    star_dict = {
        1: GeneralReview.VERY_NEGATIVE,
        2: GeneralReview.NEGATIVE,
        3: GeneralReview.NEUTRAL,
        4: GeneralReview.POSITIVE,
        5: GeneralReview.VERY_POSITIVE
    }
    resultado = analizador_sentimientos(comment)
    stars = int(resultado[0]['label'].split(' ')[0])
    return star_dict[int(resultado[0]['label'].split(' ')[0])], stars