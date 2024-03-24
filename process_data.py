import numpy as np 
import pandas as pd 
import os 

dataset_name = os.path.join('data', 'googleplaystore_user_reviews.csv')
df = pd.read_csv(dataset_name)
print("Data loaded from:", dataset_name, "with a shape of", df.shape)

columns_to_keep = ['App', 'Translated_Review', 'Sentiment']
# df['Translated_Review'] = df['Translated_Review'].str.replace(r'^["\'](.*?)["\']$', r'\1', regex=True)
df = df[columns_to_keep]

# only keep rows with sentiment of 'Positive' or 'Negative' or 'Neutral'
df = df[df['Sentiment'].isin(['Positive', 'Negative', 'Neutral'])]
print("Data shape after filtering sentiment values:", df.shape)

# drop rows with missing values
df = df.dropna(subset=['Translated_Review'])
print("Data shape after dropping missing values:", df.shape)

# drop rows with translated review of length 1
df = df[df['Translated_Review'].str.split().apply(len) > 1]
print("Data shape after filtering short reviews:", df.shape)

# # drop rows with duplicated reviews
# df = df.drop_duplicates(subset=['Translated_Review'])
# print("Data shape after dropping duplicates:", df.shape)

# save the processed data
processed_data_name = os.path.join('output', 'document_sentiment.csv')
df.to_csv(processed_data_name, index=True)
print("Data saved to:", processed_data_name, "with a shape of", df.shape)
