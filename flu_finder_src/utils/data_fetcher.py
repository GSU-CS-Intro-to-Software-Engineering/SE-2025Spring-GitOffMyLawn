import os
import sys
import requests
import pandas as pd
from dotenv import load_dotenv

# CSV URL
csv_url = "https://www.cdc.gov/bird-flu/modules/situation-summary/commercial-backyard-flocks.csv"

# Load environment variables from .env
load_dotenv()

# Get download path from .env (default to project root if not set)
# Updated to have an absolute path for download
path = os.getenv("DOWNLOAD_PATH")
script_dir = os.path.dirname(os.path.abspath(__file__)) # Get absolute path of current file
project_root = os.path.abspath(os.path.join(script_dir, "..", "..")) # Go up 2 directories (to the root)
download_path = os.path.join(project_root, path) # Append the path given in .env to the root


# Download the CSV file
def download_csv():
    print(f"Saving file to: {path}")
    response = requests.get(csv_url)
    if response.status_code == 200:
        with open(download_path, "wb") as file:
            file.write(response.content)
        print(f"CSV file downloaded to {path}")
    else:
        print("Couldn't download CSV")
        sys.exit()

def get_sorted_dataframe():
    # Load the CSV into Pandas
    df = pd.read_csv(download_path)
    
    # Convert "Outbreak Date" to datetime using the format "%m-%d-%Y" and sort the DataFrame
    df["Outbreak Date"] = pd.to_datetime(df["Outbreak Date"], format="%m-%d-%Y")
    df_sorted = df.sort_values("Outbreak Date").copy()
    
    # Change the "Outbreak Date" format to "MM/DD/YYYY"
    df_sorted["Outbreak Date"] = df_sorted["Outbreak Date"].dt.strftime("%m/%d/%Y")
    
    # Reset the index and store the old index in a column named "index"
    df_sorted.reset_index(inplace=True)
    
    # Configure Pandas to display all rows
    pd.set_option("display.max_rows", len(df_sorted))
    
    return df_sorted


# UNCOMMENT THESE TO PRINT IN CONSOLE
# download_csv()
# print(get_sorted_dataframe())