import pandas as pd
import requests
import os
from config import API_KEY

# re-fetch data 
url = f"https://api.themoviedb.org/3/trending/tv/week?api_key={API_KEY}"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["results"])

print("RAW DATA SIZE:", df.shape)


# Select useful columns
df = df[[
    "name",
    "first_air_date",
    "vote_average",
    "popularity",
    "original_language",
    "overview"
]]


# Rename columns (clean naming)
df.columns = [
    "title",
    "release_date",
    "rating",
    "popularity",
    "language",
    "description"
]


# Handle missing values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Create new feature
df["rating_category"] = df["rating"].apply(
    lambda x: "High Rated" if x >= 7 else "Medium/Low Rated"
)

print("\nCLEAN DATA SIZE:", df.shape)

print("\nCLEANED DATA SAMPLE:\n")
print(df.head())



output_dir = "/opt/airflow/data/processed"
os.makedirs(output_dir, exist_ok=True)

# Save processed data (FIXED PATH)
output_path = f"{output_dir}/trending_series_clean.csv"
df.to_csv(output_path, index=False)

print("\nSaved file at:", output_path)
print("\nTransformation completed successfully!")