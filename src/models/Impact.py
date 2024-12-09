import pandas as pd
import numpy as np

def impact_genre(movies_df):
    ###
    # Function that calculates the impact of a given genre based on the success of movies in that genre. 
    #
    # Input arguments:
    # - movies_df: Movies dataframe that contains the release date and the success of all movies in a given genre
    #
    # Output:
    # - Impact series: A timeseries that shows the impact of a genre on the movie industry. 


    # Might change this when doing exp or add it as a param of the function later.  
    linear_duration = 30

    # Surement changer le nom des colonnes pour que ca marche
    movies_df['release date'] = pd.to_datetime(movies_df['release date'])

    date_min = movies_df["release date"].min()
    date_max = movies_df["release date"].max()

    time_index = pd.date_range(start=date_min - pd.Timedelta(days=100), end= date_max +pd.Timedelta(days=100), freq='D')

    first_derivative_series = pd.Series(0.0, time_index)


    movies_df.sort_values(by=["release date"])

    for _, row in movies_df.iterrows():
        event_time = row["release date"]
        spike_value = row["success"] 

        # We first add a linear growth (positive) 
        linear_end = min(event_time + linear_duration, len(first_derivative_series))
        linear_range = np.linspace(0, spike_value, linear_end - event_time)
        first_derivative_series.iloc[event_time:linear_end] += linear_range

        # Decay, the movie starts to lose the interest of the public (Want to do exponential later)
        decay_end = min(event_time + 2*linear_duration, len(first_derivative_series))
        decay_range = -np.linspace(0, spike_value, decay_end - linear_end)
        first_derivative_series.iloc[linear_end:decay_end] += decay_range

    
    impact_series = first_derivative_series.cumsum()

    return impact_series