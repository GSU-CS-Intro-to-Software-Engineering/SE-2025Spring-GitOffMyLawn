import gspread
from google.oauth2.service_account import Credentials
from data_fetcher import get_sorted_dataframe_from_link
import pandas as pd

# Define scopes
SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]

# Load credentials from the JSON key file
creds = Credentials.from_service_account_file("./google_backend.json", scopes=SCOPES)

# Authorize gspread with the credentials
client = gspread.authorize(creds)


# --- data ---
# Open the spreadsheet by name or URL
sheet1 = client.open("data").sheet1

#! To automate, make this a daily cron job
def update_db():
    # Pull data from CDC
    df = get_sorted_dataframe_from_link("https://www.cdc.gov/bird-flu/modules/situation-summary/commercial-backyard-flocks.csv")
    # Convert to list of lists
    data = [df.columns.tolist()] + df.values.tolist()
    # Write data
    sheet1.update(values=data, range_name='A1')

def get_db():
    df = pd.DataFrame(sheet1.get_all_records())
    df.index.name = "Index"
    return df

def get_updated_db():
    update_db()
    data = sheet1.get_all_records()
    df = pd.DataFrame(data)
    return df


# --- users ---
# Open the spreadsheet by name or URL
# sheet2 = client.open("users").sheet1

# # # Read data
# users = sheet2.get_all_records()
# print(users)

# # Write data
# sheet2.update('A2', 'Updated value')



update_db()