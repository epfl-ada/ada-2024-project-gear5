import pandas as pd
from transformers import pipeline

def perform_sentiment_analysis(reviews, sa_column):
    #if invalid column name, we stop
    if sa_column not in reviews.columns:
        raise ValueError(f"The column{sa_column}doesn't exist")
    #ensure that the reviews are not too long.
    reviews[sa_column] = [
        reviews[sa_column].iloc[i][:500] if isinstance(reviews[sa_column].iloc[i], str) else reviews[sa_column].iloc[i]
        for i in range(reviews.shape[0])
    ]
    #perform sentiment analysis
    sa_analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
    reviews["sentiment"] = reviews[sa_column].apply(lambda x: sa_analyzer(x)[0]['label'] if pd.notnull(x) else None)
    reviews["sentiment_score"] = reviews[sa_column].apply(lambda x: sa_analyzer(x)[0]['score'] if pd.notnull(x) else None)
    return reviews
