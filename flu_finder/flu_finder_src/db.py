import os
import psycopg2
from dotenv import load_dotenv

# load environment variables from .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Get connection to DB using Database URL
def connect_db():
  try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Connected to database")
    return conn
  except Exception as e:
    print("Error connecting to database:", e)
    return None

# Testing connection with database
def test_query():
  conn = connect_db()
  if conn:
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    print("Database time:", cur.fetchone()[0])
    cur.close()
    conn.close()