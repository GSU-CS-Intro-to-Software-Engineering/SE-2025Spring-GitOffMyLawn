import os
import sys
import requests
import getpass
import polars as pl
from dotenv import load_dotenv

# CSV URL
csv_url = "https://www.cdc.gov/bird-flu/modules/situation-summary/commercial-backyard-flocks.csv"

# Load environment variables from .env
load_dotenv()

# Get download path from .env (default to project root if not set)
download_path = os.getenv("DOWNLOAD_PATH", os.path.join(os.getcwd(), "data.csv"))


# Download the CSV file
def download_csv():

    print(f"Saving file to: {download_path}")
    response = requests.get(csv_url)
    if response.status_code == 200:
        with open(download_path, "wb") as file:
            file.write(response.content)
        print(f"CSV file downloaded to {download_path}")
    else:
        print("Couldn't download CSV")
        sys.exit()

def get_sorted_dataframe():
    # Load the CSV into Polars
    df = pl.read_csv(download_path, try_parse_dates=True)

    # Convert "Outbreak Date" to Date type and sort
    df_sorted = df.with_columns(pl.col("Outbreak Date").str.strptime(pl.Date, "%m-%d-%Y")).sort("Outbreak Date")
    df_sorted = df_sorted.with_row_index("index")

    # Configure Polars to display all rows
    pl.Config.set_tbl_rows(len(df_sorted))

    """Returns the loaded DataFrame."""
    return df_sorted