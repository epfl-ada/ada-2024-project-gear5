import pandas as pd
# function to print the size of the dataframe
def print_df_size(name, df):
	print(name, f"- shape: {df.shape} --> {df.shape[0]} rows and {df.shape[1]} columns")

# We don't have information about inflation before 1913, so we will apply the 1913 inflation rates to the oldest movies
def inflation_date_constraint(date):
    if date.year<1913:
        return pd.Timestamp('1913-01-01')
    return date

