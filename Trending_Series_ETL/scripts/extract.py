import requests
import pandas as pd
from config import API_KEY

url = f"https://api.themoviedb.org/3/trending/tv/week?api_key={API_KEY}"

response = requests.get(url)

print("STATUS CODE:", response.status_code)

data = response.json()

results = data.get("results", [])

print("Number of shows fetched:", len(results))

df = pd.DataFrame(results)

print("\nTOP 5 TRENDING SHOWS:\n")
print(df[["name", "vote_average", "popularity", "first_air_date"]].head())