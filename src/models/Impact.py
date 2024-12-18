import pandas as pd
import numpy as np
from scipy.optimize import curve_fit


def exponential_func(x, a, b, c):
    return a * np.exp(b * x) + c

def impact_genre(movies_df):
    ###
    # Function that calculates the impact of a given genre based on the success of movies in that genre. 
    #
    # Input arguments:
    # - movies_df: Movies dataframe that contains the release date and the success of all movies in a given genre
    #
    # Output:
    # - Impact series: A timeseries that shows the impact of a genre on the movie industry. 

    
    # Surement changer le nom des colonnes pour que ca marche
    movies_df['combined_release_date'] = pd.to_datetime(movies_df['combined_release_date'], errors='coerce')
    movies_df = movies_df.dropna(subset=['combined_release_date'])
    movies_df = movies_df.sort_values(by=["combined_release_date"])

    date_min = movies_df["combined_release_date"].min()
    date_max = movies_df["combined_release_date"].max()

    mean_success_genre = movies_df["success_score"].mean()

    time_index = pd.date_range(
        start = date_min - pd.Timedelta(days=100), 
        end = date_max + pd.Timedelta(days=100), 
        freq = 'D'
    )

    first_derivative_series = pd.Series(0.0, time_index)

    for _, row in movies_df.iterrows():
        event_time = row["combined_release_date"]
        spike_value = row["success_score"] 

        # We make sure that more successful movies have more of an impact. Want the transformation we apply to still be continuous. 
        spike_value = 10 * (1 / (1 + np.exp(-0.5 * (spike_value - (mean_success_genre + 2)))))
            
        # We change the duration of the linear growth depending on the impact of the movie 
        base_duration = 30  
        linear_duration = int(base_duration * (1 + spike_value*4))


        # We first add a linear growth. The length of this linear growth depends on the success of the movie.
        linear_end_time = event_time + pd.Timedelta(days = linear_duration)
        if linear_end_time > first_derivative_series.index[-1]:
            linear_end_time = first_derivative_series.index[-1]

        linear_range = np.linspace(0, spike_value, (linear_end_time - event_time).days + 1)
        first_derivative_series.loc[event_time:linear_end_time] += linear_range
        
        # Decay, the movie starts to lose the interest of the public (Want to do exponential later)
        decay_end_time = event_time + pd.Timedelta(days = 2 * linear_duration)
        if decay_end_time > first_derivative_series.index[-1]:
            decay_end_time = first_derivative_series.index[-1]

        decay_range = -np.linspace(0, spike_value, (decay_end_time - linear_end_time).days + 1)
        first_derivative_series.loc[linear_end_time:decay_end_time] += decay_range

    
    impact_series = first_derivative_series.cumsum()

    # We fit an polynomial to remove the trend -> More movies = more success
    time_numeric = np.arange(len(impact_series))
    coefficients = np.polyfit(time_numeric, impact_series, deg=2)
    polynomial_trend = np.polyval(coefficients, time_numeric)
    impact_series = impact_series - polynomial_trend

    impact_series = (impact_series)/100000
    
    return impact_series