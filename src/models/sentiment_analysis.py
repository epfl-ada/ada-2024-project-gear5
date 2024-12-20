import pandas as pd
import torch
from tqdm import tqdm
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification


tqdm.pandas()

def sentiment_analysis(reviews, sa_column, item_id, index ,output_file):
    """
    Perform sentiment analysis on a given DataFrame of reviews.
    
    Parameters :
        reviews (pd.DataFrame) : 
            DataFrame containing the reviews.
        sa_column (str) : 
            The name of the column in the DataFrame that contains the text reviews.
        item_id (str) : 
            The name of the column in the DataFrame that contains the item IDs.
        index (str) : 
            The name of the column in the DataFrame that contains the index.
        output_file (str) : 
            The path to the output file where the results will be saved.
    
    Returns:
        pd.DataFrame : 
            DataFrame with the sentiment analysis results.
    Raises:
        ValueError : 
            If any of the specified columns do not exist in the DataFrame.
    """
    
    
    #ensure that the columns exist
    for column in [sa_column, item_id, index]:
        if column not in reviews.columns:
            raise ValueError(f"The column {column} doesn't exist")
    # Loading a Pre-Trained Model from HuggingFace Hub
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    print(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    #ensure that the reviews are not too long.
    reviews[sa_column] = [
        reviews[sa_column].iloc[i][:512] if isinstance(reviews[sa_column].iloc[i], str) else reviews[sa_column].iloc[i]
        for i in range(reviews.shape[0])
    ]
    #intialize the sentiment analysis classifier
    device = 0 if torch.cuda.is_available() else -1
    sa_classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, device=device)
    sa = apply_sentiment_analysis(sa_classifier, reviews, sa_column, item_id, index, output_file)
    return sa

def apply_sentiment_analysis(sa_classifier, reviews, sa_column, item_id, index, output_file):
    """
    Apply sentiment analysis to a specified column in a DataFrame and save the results to a CSV file.
    
    Parameters :
        sa_classifier (callable) : 
            A sentiment analysis classifier function that takes a string input and returns a sentiment score.
        reviews (pd.DataFrame) : 
            A pandas DataFrame containing the reviews data.
        sa_column (str) : 
            The name of the column in the DataFrame that contains the text to analyze.
        item_id (str) : 
            The name of the column in the DataFrame that contains the item IDs.
        index (str) : 
            The name of the column in the DataFrame that should be used as the index.
        output_file (str) : 
            The file path where the resulting DataFrame with sentiment analysis should be saved as a CSV file.
    
    Returns :
        pd.DataFrame : 
            A DataFrame containing the sentiment analysis results along with the specified item ID and index columns.
    """
    
    reviews["sentiment_analysis"] = reviews[sa_column].progress_apply(lambda x: sa_classifier(x)[0] if pd.notnull(x) else None)
    columns_to_keep = ["sentiment_analysis", item_id, index]
    reviews = reviews[columns_to_keep]
    reviews.to_csv(output_file, index=True)
    return reviews