import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

def sentiment_analysis(reviews, sa_column):
    # if invalid column name, we stop
    if sa_column not in reviews.columns:
        raise ValueError(f"The column{sa_column}doesn't exist")
    # Loading a Pre-Trained Model from HuggingFace Hub
    model_name = "cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    #ensure that the reviews are not too long.
    reviews[sa_column] = [
        reviews[sa_column].iloc[i][:512] if isinstance(reviews[sa_column].iloc[i], str) else reviews[sa_column].iloc[i]
        for i in range(reviews.shape[0])
    ]
    #intialize the sentiment analysis classifier
    sa_classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    sa = apply_sentiment_analysis(sa_classifier, reviews, sa_column)
    return sa

def apply_sentiment_analysis(sa_classifier, reviews, sa_column):
    reviews["sentiment_analysis"] = reviews[sa_column].apply(lambda x: sa_classifier(x)[0] if pd.notnull(x) else None)
    reviews["sentiment"] = reviews["sentiment_analysis"].apply(lambda x: x['label'] if pd.notnull(x) else None)
    reviews["sentiment_score"] = reviews["sentiment_analysis"].apply(lambda x: x['score'] if pd.notnull(x) else None)
    reviews.drop(columns=["sentiment_analysis"], inplace=True)
    return reviews

