# etl.py
import pandas as pd
from sqlalchemy import create_engine
from db_config import DB_URI

# Step 1: Load the CSV
df = pd.read_csv("data/data.csv")

# Step 2: Clean column names (optional)
df.columns = [c.lower().replace(" ", "_") for c in df.columns]

# Step 3: Convert date columns (if any)
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Step 4: Connect to PostgreSQL
engine = create_engine(DB_URI)

# Step 5: Write the data to a table
df.to_sql("spotify_data", engine, if_exists="replace", index=False)

print("✅ Data loaded to PostgreSQL successfully.")
