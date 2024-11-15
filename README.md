# ADA 2024 - Gear 5
# Evolution of cinema through the years, finding the golden age.

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

In addition to the original dataset, we are using the movielens and tmdb datasets. 
The movielens dataset gives us access to reviews and ratings for a wide range of movies. 
The TMBb dataset allows us to have a more complete version, closer in style to the original CMU Movie one.

## Methods

### Part 1 - Defining the "Golden Age" thanks to the success metric

For our project, we intend on defining the relative success of a movie by assessing multiple statistics. These metrics include:
- One can identify the "Golden Age" based on financial success by pointing out the period when the cinema industry generated the most revenue adjusted to inflation. Analysis box office data by year and thus visualize trends to identify periods of high financial success.
- Movie ratings from MovieLens (From the MovieLens dataset): This metric gives the general grade given to each movie on the MovieLens website. 
- User movie ratings (From the MovieLens dataset): This metric gives the grade given by individual users on the MovieLens website. 
- Reviews sentiment analysis (From the MovieLens dataset): From user reviews collected on the MovieLens website, we want to run a sentiment analysis to find if they are positive or negative, and thus assess the evolution of sentiments along the years. For the sentiment analysis, we want to use FacebookAI's RoBERTa-base, a pretrained tokenizer and model distributed by HugginFace.

### Part 2 - Time-related trends analysis per genre and country

Once the robust success metric is created, we want to apply it to all the movies in our combined dataset. This will help us to indicate how movie success (measured by box office, ratings, and sentiment) changes over time by genre and country, helping to identify shifts in dominant genres and regions, and pinpoint key cinematic "eras."
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

## Proposed timeline and organization

Week 9 -- 11/11 - 17/11: 
- [x] Finding the additional datasets needed for the idea
- [ ] Combining the dataset and cleaning the data
- [ ] Have Proofs of concepts for all the methods we want to use in the project
- [x] Project P2 deadline

Week 10 -- 18/11 - 24/11: 
- [ ] Running the sentiment analysis on the movie critics: **Mahmoud**, **Mathieu**
- [ ] Defining the "success" metric and testing it on selected movies to see how well it works: **Loïc**, **Léo**, **Bastien**

Week 11 -- 25/11 - 01/12: 
- [ ] Finish the first part of the project
    - [ ] Success yearly arrays analysis to find "golden ages": **Léo**, **Mathieu**, **Bastien**
    - [ ] Vizualisation of the results found: **Loïc**, **Mahmoud**

Week 12 -- 02/12 - 08/12: 
- [ ] Data vizualisation for second part: **Mahmoud**, **Bastien**
- [ ] Using predictive models on the success yearly arrays for part 3: **Léo**, **Loïc**, **Mathieu**

Week 13 -- 09/12 - 15/12: 
- [ ] Start writing the story. Will need to complete work done with more vizualisations: **Léo**, **Loïc**, **Mahmoud**

Week 14 -- 16/12 - 20/12: 
- [ ] Project P3 deadline
    - [ ] Finish the story we want to tell: **Bastien**, **Mathieu**

## Project Structure

The directory structure of new project looks like this:

```
├── data                        <- Project data files
│
├── src                         <- Source code
│   ├── data                            <- Data directory
│   ├── models                          <- Model directory
│   ├── utils                           <- Utility directory
│   ├── scripts                         <- Shell scripts
│
├── tests                       <- Tests of any kind
│
├── results.ipynb               <- a well-structured notebook showing the results
│
├── .gitignore                  <- List of files ignored by git
├── pip_requirements.txt        <- File for installing python dependencies
└── README.md