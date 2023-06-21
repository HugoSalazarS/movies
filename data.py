import pandas as pd
import datetime


# load the data
mv = pd.read_csv('datasets/cleaned_data/movies_cleaned.csv')
credits = pd.read_csv('datasets/cleaned_data/credits_cleaned.csv')

# Join the datasets
df = pd.merge(mv, credits, on=['id', 'id'], how='inner')

# set the date format 
df['release_date'] = pd.to_datetime(df['release_date']).dt.strftime("%Y-%B-%d")
df['release_day'] = pd.to_datetime(df['release_date']).dt.strftime('%A')
