"""
import pandas as pd
from tqdm import tqdm
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch

tqdm.pandas()

def sentiment_analysis(reviews, sa_column, id, output_file):
    # if invalid column name, we stop
    if sa_column not in reviews.columns:
        raise ValueError(f"The column{sa_column}doesn't exist")
    # Loading a Pre-Trained Model from HuggingFace Hub
    #model_name = "cardiffnlp/twitter-roberta-base-sentiment"
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    print(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    #ensure that the reviews are not too long.
    reviews[sa_column] = [
        reviews[sa_column].iloc[i][:513] if isinstance(reviews[sa_column].iloc[i], str) else reviews[sa_column].iloc[i]
        for i in range(reviews.shape[0])
    ]
    #intialize the sentiment analysis classifier
    device = 0 if torch.cuda.is_available() else -1
    sa_classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, device=device)
    sa = apply_sentiment_analysis(sa_classifier, reviews, sa_column, id, output_file)
    return sa

def apply_sentiment_analysis(sa_classifier, reviews, sa_column, id, output_file):
    reviews["sentiment_analysis"] = reviews[sa_column].progress_apply(lambda x: sa_classifier(x)[0] if pd.notnull(x) else None)
    #reviews["sentiment"] = reviews["sentiment_analysis"].apply(lambda x: x['label'] if pd.notnull(x) else None)
    #reviews["sentiment_score"] = reviews["sentiment_analysis"].apply(lambda x: x['score'] if pd.notnull(x) else None)
    columns_to_keep = ["sentiment_analysis", id]
    reviews = reviews[columns_to_keep]
    reviews.to_csv(output_file, index=True)
    return reviews
"""

import pandas as pd
from tqdm import tqdm
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from datasets import Dataset
import torch

tqdm.pandas()

def sentiment_analysis(reviews, sa_column, id, output_file):
    # if invalid column name, we stop
    if sa_column not in reviews.columns:
        raise ValueError(f"The column {sa_column} doesn't exist")
    # Loading a Pre-Trained Model from HuggingFace Hub
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    print(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    # Ensure that the reviews are not too long.
    reviews[sa_column] = [
        reviews[sa_column].iloc[i][:512] if isinstance(reviews[sa_column].iloc[i], str) else reviews[sa_column].iloc[i]
        for i in range(reviews.shape[0])
    ]
    # Initialize the sentiment analysis classifier with GPU support
    device = 0 if torch.cuda.is_available() else -1
    sa_classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, device=device)

    # Convert the DataFrame to a Dataset
    dataset = Dataset.from_pandas(reviews)

    # Apply sentiment analysis in parallel
    def apply_sa(batch):
        results = sa_classifier(batch[sa_column])
        return {"sentiment_analysis": results}

    dataset = dataset.map(apply_sa, batched=True, batch_size=32)

    # Convert the Dataset back to a DataFrame
    reviews = dataset.to_pandas()

    # Keep only the necessary columns
    columns_to_keep = ["sentiment_analysis", id]
    reviews = reviews[columns_to_keep]
    reviews.to_csv(output_file, index=True)
    return reviews