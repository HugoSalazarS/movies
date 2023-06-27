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

# Create actor_name_funct for the API function
df['actor_name_funct'] = df['actor_name']

# Transform the list columns
import ast
columns_lists = ['countrie_name', 'iso_lang', 'lang_name', 'character', 'actor_name', 'genre', 'iso', 'companies_name']  # list of columns with lists

for columna in columns_lists:
    df[columna] = df[columna].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)



