import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv("/opt/airflow/data/processed/trending_series_clean.csv")
# Database connection
username = "postgres"
password = "zafar"
host = "host.docker.internal"
port = "5432"
database = "Trending_Series_db"

engine = create_engine(
    "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow"
)

# Load data into SQL table
df.to_sql(
    "trending_series",
    engine,
    if_exists="append",
    index=False
)

print("Data successfully loaded into PostgreSQL!")