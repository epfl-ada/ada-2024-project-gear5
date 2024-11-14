# ADA 2024 - Gear 5


# Evolution of cinema through the years, finding the golden age.

## Abstract


## Research questions
1. What were some of the "golden ages" of cinema through the years? (sorted by movie genre and country)
2. What caused the success and the downfall of these "golden ages"? Can the success of certain genres be traced back to single movies?
3. What are some of the main differences between these golden ages and the movie industry now?
4. Is it possible to predict the next cinema golden age?

## Additional datasets
In addition to the original dataset, we are using the movielens dataset. This dataset gives us access to reviews and ratings for a wide range of movies. (Link: https://grouplens.org/datasets/movielens/) 


## Methods

### Part 1 - Defining the success metric
For our project, we intend on defining the relative success of a movie by combining multiple statistics into a single metric. These statistics include:
- Movie gross revenue (From the CMU movie dataset): This metrics indicates the revenue generated by movies. It could already give a good idea of the "success" of a movie, but we choose to add other statistics related to critical acclaim to make our metric more robust to the state of the movie industry as a whole. 
- Movie ratings from MovieLens (From the MovieLens dataset): This metric gives the general grade given to each movie on the MovieLens website. 
- User movie ratings (From the MovieLens dataset): This metric gives the grade given by individual users on the MovieLens website. 
- Reviews sentiment analysis (From the MovieLens dataset): From user reviews collected on the MovieLens website, we want to run a sentiment analysis to find if they are positive or negative. 

For the sentiment analysis, we want to use [...].



### Part 1 - Change point analysis on timeseries
Once we have a robust success metric, we want to apply it to all the movies in our combined dataset. We will then group movies by the country in which they were produced and by their genre (NB: Movies might have more then one genre, we are going to make them appear in all their genre). 

This is going to give us a multitude of timeseries of the success. We are going to analyze these timeseries to find major change points indicating the beginning or the end of a "Golden age". We have not yet chosen the method we are going to use for the project as multiple could be used, such as: 
- a
- b
- c


### Part 2 - 
a


### Part 3 - Success prediction
Finally, in the third part of our project, we are going to use the timeseries derived in part 1 to make some predictions. The aim is to predict the future state of the movie industry in terms of success. To do so, we are going to compare the performance of these different algorithms:
- Polynomial regression / Ridge regression: Might do the algorithms ourselves
- Autoregressive integrated moving average (ARIMA): "statsmodel" package in python




## Proposed timeline
Week 9 -- 11/11 - 17/11: 
- [x] Finding the additional datasets needed for the idea
- [ ] Combining the dataset and cleaning the data
- [ ] Have Proofs of conecepts for all the methods we want to use in the project
- [ ] Project P2 deadline

Week 10 -- 18/11 - 24/11: 
- [ ] Focus on Homework 2
- [ ] Running the sentiment analysis on the movie critics
- [ ] Defining the "success" metric and testing it on selected movies to see how weel it works

Week 11 -- 25/11 - 01/12: 
- [ ] Focus on Homework 2
- [ ] Finish the first part of the project
    - [ ] Timeseries analysis to find "golden ages"
    - [ ] Vizualisation of the results found

Week 12 -- 02/12 - 08/12: 
- [ ] Data vizualisation for second part
- [ ] Using predictive models on the timeseries for part 3

Week 13 -- 09/12 - 15/12: 
- [ ] Start writing the story. Will need to complete work done with more vizualisations

Week 14 -- 16/12 - 20/12: 
- [ ] Project P3 deadline
    - [ ] Finish the story we want to tell


## Work breakdown
Bastien: 

Leo:

Loic:

Mahmoud:

Matthieu:


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
```

## Questions for the TA