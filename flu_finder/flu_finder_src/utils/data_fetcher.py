import os
import sys
import requests
import getpass
import polars as pl
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# CSV URL
csv_url = "https://www.cdc.gov/bird-flu/modules/situation-summary/commercial-backyard-flocks.csv"

# Get download path from .env (default to project root if not set)
download_path = os.getenv("DOWNLOAD_PATH", os.path.join(os.getcwd(), "data.csv"))

# Download the CSV file
response = requests.get(csv_url)
if response.status_code == 200:
    with open(download_path, "wb") as file:
        file.write(response.content)
    print(f"CSV file downloaded to {download_path}")
else:
    print("Couldn't download CSV")
    sys.exit()

# Load the CSV into Polars
df = pl.read_csv(download_path, try_parse_dates=True)

# Convert "Outbreak Date" to Date type and sort
df = df.with_columns(pl.col("Outbreak Date").str.strptime(pl.Date, "%m-%d-%Y")).sort("Outbreak Date")

# Configure Polars to display all rows
pl.Config.set_tbl_rows(len(df))

# Sort by year of "Outbreak Date" and print
# df_sorted = df.sort(pl.col("Outbreak Date").dt.year())
# print(df_sorted)

# Method to keep data loading centrally located here but we can reuse it in other files
def get_dataframe():
    return df