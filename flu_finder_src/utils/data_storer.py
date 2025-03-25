import os
import json
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

load_dotenv()
json_creds = json.loads(os.getenv("GOOGLE_CREDS_JSON"))

# Define scopes
SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]

# Load credentials from the JSON key file
creds = Credentials.from_service_account_info(json_creds, scopes=SCOPES)

# Authorize gspread with the credentials
client = gspread.authorize(creds)


# --- data ---
# Open the spreadsheet by name or URL
sheet1 = client.open("data").sheet1

data = sheet1.get_all_records()
print(data)

# Write data
# sheet1.update('A2', 'Updated value')


# --- users ---
# Open the spreadsheet by name or URL
sheet2 = client.open("users").sheet1

# # Read data
users = sheet2.get_all_records()
print(users)

# # Write data
# sheet2.update('A2', 'Updated value')

