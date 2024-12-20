# ADA 2024 - Gear 5: Evolution of cinema through the years, finding the golden age

 
**Project Mentor:** [Shuo Wen](http://personnes.epfl.ch/shuo.wen) ([Email](shuo.wen@epfl.ch)),
**Authors:** Mahmoud Dokmak, Matthieu Borello, Léo Brunneau, Loïc Domingos, Bastien Armstrong

<hr style="clear:both">



## Quickstart

```bash
# clone project
git clone https://github.com/epfl-ada/ada-2024-project-gear5.git
cd <project repo>

# [OPTIONAL] create conda environment
conda create -n <env_name> python=3.12
conda activate <env_name>

# install requirements
pip install -r pip_requirements.txt
```

## Abstract

This project delves into the evolution of cinema to explore whether a “Golden Age” has existed and to identify the key factors that define success across eras. By analyzing historical and contemporary trends in film production, genre popularity, and global appeal, we aim to uncover patterns that reflect shifts in cinematic influence and cultural resonance over time. Our approach considers both the artistic and economic dimensions of the film industry, examining how certain genres, themes, and regions rise to prominence and shape cinematic eras. Ultimately, we seek to understand where the current landscape fits within cinema’s broader history and what trends may lie ahead. Through data-driven insights, we hope to tell a compelling story of cinema’s dynamic journey and its role in reflecting and shaping society across decades.

## Research questions

1. Has there ever been a "Golden Age" of cinema ? Which metrics are important to evaluate the global success of the cinema industry and, therefore, a potential "Golden Age" ?

2. What were the specific ages of cinema throughout the years ? Is it possible to observe time-related trends about a specific genre or country ?

3. What about now ? Are we in a specific era ? What are the past decade trends and what could we infer from this ? Can we build a strong metric that predicts a future trend and, therefore, a movie success ?

## Additional datasets
In addition to the original dataset [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/), we are using the [MovieLens Tag Genome Dataset 2021](https://grouplens.org/datasets/movielens/)  and [Full TMDB Movies Dataset 2024](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies/data) datasets.
The[MovieLens Tag Genome Dataset 2021](https://grouplens.org/datasets/movielens/) dataset gives us access to reviews and ratings for a wide range of movies.
The TMBb dataset allows us to enrich our original dataset by offering a dataset that is closer in style to the original [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) one.

## Methods

### Part 1 - Defining the "Golden Age" thanks to the success metric

For our project, we intend on defining the relative success of a movie by assessing multiple statistics. These metrics include:

- The popularity of a movie: We get a popularity score from the TMDb dataset, which is a metric that takes into account the following:
  - Release date
  - Number of users who added it to their "watchlist" for the day
  - Number of users who marked it as a "favourite" for the day
  - Number of views for the day
  - Number of votes for the day
  - Total number of votes
  - Vote average
  - Previous day's popularity score
- The box office revenue of a movie adjusted for inflation. One can identify the "Golden Age" based on financial success by pointing out the period when the cinema industry generated the most revenue adjusted to inflation.
- User movie ratings (from the MovieLens dataset). This metric gives the grade given by individual users on the MovieLens website. Viewers opinions are important to assess the success of a movie.
- Reviews sentiment analysis (from [MovieLens Tag Genome Dataset 2021](https://grouplens.org/datasets/movielens/)) dataset: We run sentiment analysis on reviews, defining if they are positive or negative, and thus assess the again the viewers' point of view. For the sentiment analysis, we use a pretrained Bert model and a pretrained tokenizer available on HugginFace [here](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english).

We define the "Golden Age" per genre as the decade where the average success score is the highest. We will also look at the average success score per year to identify the "Golden Age" of cinema in general. This will allow us to identify the most successful genres and periods in cinema history.

### Part 2 - Time-related trends analysis per genre and country

Once the robust success metric is created, we want to apply it to all the movies in our combined dataset. This will help us to indicate how movie success (measured by popularity, box office, ratings, and sentiment) changes over time by genre, helping to identify shifts in dominant genres and regions, and pinpoint key cinematic "eras."
The data will be preprocessed by grouping movies based on their genres (handling multi-genre films) and countries of origin. Then, we will calculate success metrics for each movie, aggregated by year, genre, and country.
Using these metrics, we will create time-series data to track the success of different genres and countries over time. For each group, we will calculate the average success score, total box office revenue (adjusted for inflation), and the number of films produced.
These trends will be analyzed in order to identify which genres and countries have been most successful at different times. For example, we might see action films rise in the 1980s or how Bollywood’s global influence grew in the 2000s. We’ll also look for cultural patterns, like the dominance of war films during WWII.
To visualize these trends, we can use line charts for success scores, stacked bar charts for film production by genre or country, and heatmaps for sentiment analysis over time. This will help us identify key shifts in genre and country dominance.
This analysis will allow us to define cinematic "eras" based on dominant genres or countries, such as the Golden Age of Hollywood or the rise of global cinema in the 21st century.

### Part 3 - What about now ?

Here, our goal is to assess the current state of the film industry by analyzing trends from the past decade and using this data to predict future movie success and industry directions.
First, the analysis will focus on movies released in the last 10 years. By filtering the data to this timeframe, we can analyze key metrics such as box office performance, genre popularity, movie runtimes, and the impact of emerging trends like streaming. This will give us a clear picture of where the industry stands today.
Next, we will examine the current trends in the industry. This includes identifying which genres are most successful right now, such as superhero films or streaming-exclusive releases. We will also look for new genres or countries that are gaining popularity. Additionally, tracking movie length trends will help determine whether films are getting longer or shorter, and we will explore how streaming platforms are influencing traditional theatrical releases.
To predict future trends, we will apply predictive models. Polynomial Regression or Ridge Regression could be used to forecast movie success based on factors like genre, cast, and release timing. We may also use ARIMA (Autoregressive Integrated Moving Average) for time-series forecasting to predict box office trends or shifts in genre popularity.
The key insights from this analysis will offer conclusions about the future direction of the film industry. This includes identifying potential growth areas or disruptions, such as the rise of new genres, international markets, or emerging technologies in filmmaking and distribution.

## Project Structure

The directory structure of new project looks like this:

```text
├── data                        <- Project data files
│   │
│   ├── CMU_movie                       <- Original CMU movies dataset
│   ├── Converter                       <- Converter dataset used to match movie IDs
│   ├── MovieLens                       <- MovieLens dataset with ratings and reviews
│   ├── MovieSummaries                  <- Movie Summaries
│   ├── TMDBMovies                      <- TMDB Movies dataset to enrich the original dataset
│
├── plots                       <- Our html plots
├── src                         <- Source code
│   ├── models    
│   │   │
│   │   ├── ARIMA.py                        <- Used to run the ARIMA algo
│   │   ├── PolynomialRegression.py         <- Used to run the polynomial regression 
│   │   ├── Impact.py                       <- Used to calculate impact of a given genre
│   │   ├── sentiment_analysis.py           <- Used to calculate impact of a given genre
│   │  
│   ├── utils                           <- Utility directory
│   │   │
│   │   ├── print_prediction.py             <- Printing prediction proof of concept
│   │   ├── result_utils.py                 <- Utilities
│
├── .gitignore                  <- List of files ignored by git
├── requirements.txt            <- File for installing python dependencies
├── data.ipynb                  <-  a well-structured notebook used to load and preprocess the data
├── methods.ipynb               <- a well-structured notebook showing the methods used
├── result.ipynb                <- a well-structured notebook showing our results
├── resultsM2.ipynb             <- a well-structured notebook showing our results for milestone 2
├── sentiment_analysis.ipynb    <- a well-structured notebook to run sentiment analysis
├── READMEM2.md                 <- The Milestone 2 README.
└── README.md                   <- The top-level README for developers using this project.

```
