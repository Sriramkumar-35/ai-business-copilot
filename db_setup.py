"""
db_setup.py
------------
Loads the sample sales CSV into a SQLite database (sales.db).
Run this once before starting the app:
    python db_setup.py
"""

import sqlite3
import pandas as pd
import os

CSV_PATH = os.path.join("data", "sample_sales.csv")
DB_PATH = "sales.db"
TABLE_NAME = "sales"


def build_database():
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(
            f"Could not find {CSV_PATH}. Make sure your dataset is in the data/ folder."
        )

    df = pd.read_csv(CSV_PATH)

    # Basic cleaning
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df = df.dropna()

    conn = sqlite3.connect(DB_PATH)
    df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
    conn.close()

    print(f"✅ Database created: {DB_PATH}")
    print(f"✅ Table '{TABLE_NAME}' loaded with {len(df)} rows and columns: {list(df.columns)}")


if __name__ == "__main__":
    build_database()
