import os
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()


SHEET_ID = os.getenv("SHEET_ID")

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets', 
    'https://www.googleapis.com/auth/drive'
    ]

SERVICE_ACCOUT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")

CREDENTIALS = Credentials.from_service_account_file(SERVICE_ACCOUT_FILE, scopes=SCOPES)

def get_google_sheet_df():

    service = build('sheets', 'v4', credentials=CREDENTIALS)

    sheet = service.spreadsheets()

    range = 'A:G'

    sheet_read = sheet.values().get(spreadsheetId=SHEET_ID, range = range).execute()

    sheet_values = sheet_read.get('values',  [])

    sheet_df = pd.DataFrame(sheet_values[1:],columns=sheet_values[0])

    return sheet_df

if __name__ == '__main__':
    test = get_google_sheet_df()

    print(test)