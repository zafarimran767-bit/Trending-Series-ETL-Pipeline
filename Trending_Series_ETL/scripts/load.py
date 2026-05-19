import pandas as pd
import os
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv("/opt/airflow/data/processed/trending_series_clean.csv")
# Database connection
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
db = os.getenv("POSTGRES_DB")

engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
)

# Load data into SQL table
df.to_sql(
    "trending_series",
    engine,
    if_exists="append",
    index=False
)

print("Data successfully loaded into PostgreSQL!")