# ADA 2024 - Gear 5
# Evolution of cinema through the years, finding the golden age.

## Abstract
This project delves into the evolution of cinema to explore whether a “Golden Age” has existed and to identify the key factors that define success across eras. By analyzing historical and contemporary trends in film production, genre popularity, and global appeal, we aim to uncover patterns that reflect shifts in cinematic influence and cultural resonance over time. Our approach considers both the artistic and economic dimensions of the film industry, examining how certain genres, themes, and regions rise to prominence and shape cinematic eras. Ultimately, we seek to understand where the current landscape fits within cinema’s broader history and what trends may lie ahead. Through data-driven insights, we hope to tell a compelling story of cinema’s dynamic journey and its role in reflecting and shaping society across decades.

## Research questions
1. Has there ever been a "Golden Age" of cinema ? Which metrics are important to evaluate the global success of the cinema industry and, therefore, a potential "Golden Age" ?

2. What were the specific ages of cinema throughout the years ? Is it possible to observe time-related trends about a specific genre or country ?

3. What about now ? Are we in a specific era ? What are the past decade trends and what could we infer from this ? Can we build a strong metric that predicts a future trend and, therefore, a movie success ?

## Additional datasets
In addition to the original dataset, we are using the movielens and tmdb datasets. 
The movielens dataset gives us access to reviews and ratings for a wide range of movies.[1^]
The tmdb dataset allows us to have a more complete version, closer in style to the original CMU Movie one.[2^]


## Methods
### Part 1 - Defining the "Golden Age" thanks to the success metric
For our project, we intend on defining the relative success of a movie by assessing multiple statistics. These metrics include:
- One can identify the "Golden Age" based on financial success by pointing out the period when the cinema industry generated the most revenue adjusted to inflation. Analysis box office data by year and thus visualize trends to identify periods of high financial success.
- Movie ratings from MovieLens (From the MovieLens dataset): This metric gives the general grade given to each movie on the MovieLens website. 
- User movie ratings (From the MovieLens dataset): This metric gives the grade given by individual users on the MovieLens website. 
- Reviews sentiment analysis (From the MovieLens dataset): From user reviews collected on the MovieLens website, we want to run a sentiment analysis to find if they are positive or negative, and thus assess the evolution of sentiments along the years. For the sentiment analysis, we want to use FacebookAI's RoBERTa-base, a pretrained tokenizer and model distributed by HugginFace.



### Part 2 - Time-related trends analysis per genre and country
Once the robust success metric is created, we want to apply it to all the movies in our combined dataset. One way to proceed is to group movies by the country in which they were produced, by their respective genre (NB: Movies might have more then one genre, we are going to make them appear in every genre they're assigned to.) and by the year they were produced in. From this, we are going to create arrays to track the evolution of the success of movies genres per country on a yearly basis. This is going to give us a multitude of "yearly success" arrays. These timeseries could be very useful to find major change points indicating the beginning or the end of a era.

### Part 3 - What about now ?
Finally, in the third part of our project, only the subset of the last decade of movie prediction will be used to assess the state of the industry, what genre is dominating, new prevalent movie run time, or even a new key player in the industry.
We are also going to use the insight we have gathered before through our thorough analysis to make some predictions about the direction of our lovely ship. To do so, we are going to compare the performance of these different algorithms:
- Polynomial regression / Ridge regression: Might do the algorithms ourselves
- Autoregressive integrated moving average (ARIMA): "statsmodel" package in python


## Proposed timeline
Week 9 -- 11/11 - 17/11: 
- [x] Finding the additional datasets needed for the idea
- [ ] Combining the dataset and cleaning the data
- [ ] Have Proofs of concepts for all the methods we want to use in the project
- [x] Project P2 deadline

Week 10 -- 18/11 - 24/11: 
- [ ] Running the sentiment analysis on the movie critics
- [ ] Defining the "success" metric and testing it on selected movies to see how well it works

Week 11 -- 25/11 - 01/12: 
- [ ] Finish the first part of the project
    - [ ] Success yearly arrays analysis to find "golden ages"
    - [ ] Vizualisation of the results found

Week 12 -- 02/12 - 08/12: 
- [ ] Data vizualisation for second part
- [ ] Using predictive models on the success yearly arrays for part 3

Week 13 -- 09/12 - 15/12: 
- [ ] Start writing the story. Will need to complete work done with more vizualisations

Week 14 -- 16/12 - 20/12: 
- [ ] Project P3 deadline
    - [ ] Finish the story we want to tell

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

## References

[1^] : https://grouplens.org/datasets/movielens/
[2^] : https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies


to update
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