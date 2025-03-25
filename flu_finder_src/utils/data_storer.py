import gspread
from google.oauth2.service_account import Credentials
from data_fetcher import get_sorted_dataframe_from_link

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

# Pull data from CDC
df = get_sorted_dataframe_from_link("https://www.cdc.gov/bird-flu/modules/situation-summary/commercial-backyard-flocks.csv")

# Fix: Format Timestamp columns
df["Outbreak Date"] = df["Outbreak Date"].dt.strftime("%Y-%m-%d")

# Convert to list of lists
data = [df.columns.tolist()] + df.values.tolist()

# Write data
sheet1.update(values=data, range_name='A1')

# File output
data = sheet1.get_all_records()
print(data)


# --- users ---
# Open the spreadsheet by name or URL
# sheet2 = client.open("users").sheet1

# # # Read data
# users = sheet2.get_all_records()
# print(users)

# # Write data
# sheet2.update('A2', 'Updated value')

