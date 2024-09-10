# flowcells/google_sheet_utils.py
import logging
import uuid
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request


def get_google_sheet_data(spreadsheet_id, sheet_name, creds):
    """
    Fetches data from a specified Google Sheets document.

    Args:
        spreadsheet_id (str): The unique identifier of the Google Sheets document.
        sheet_name (str): The name of the specific sheet within the Google Sheets document.
        creds (google.oauth2.credentials.Credentials): The credentials object required to authenticate the API request.

    Returns:
        list[list[int]]: A list of rows where each row is a list of integers representing the cell values.
        Returns None if an error occurs during the fetch operation.

    Raises:
        googleapiclient.errors.HttpError: If there is an error with the API request (e.g., invalid spreadsheet ID or insufficient permissions).
        ValueError: If the data fetched from the sheet contains non-integer values that cannot be cast to integers.

    Description:
        - The function builds a Google Sheets API v4 service using the provided credentials.
        - It then constructs the range of data to retrieve (from cell A1 to Z of the specified sheet).
        - The function attempts to fetch the sheet data using the Sheets API.
        - If successful, it processes the data by converting each cell's value into an integer.
        - If an error occurs (e.g., network issues, invalid spreadsheet ID), it prints the error message and returns None.
    """
    service = build('sheets', 'v4', credentials=creds)
    range_name = f'{sheet_name}!A1:Z'
    
    try:
        sheet = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        data = sheet.get('values', [])
        return [[int(cell) for cell in row] for row in data]
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def authenticate_and_get_credentials():
    creds = None
    creds_path = r'C:\Users\chied\Desktop\DnaMicroTasks\djangoDemo - Copy\djangoBackend\islandGrid\demo\dataProcessing\credentials.json'  # Replace with actual path to your credentials.json
    token_path = r'C:\Users\chied\Desktop\DnaMicroTasks\djangoDemo - Copy\djangoBackend\islandGrid\demo\dataProcessing\token.json'  # Path to store token.json
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # Check if token.json file exists to load credentials
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    # If there are no valid credentials, or if the credentials are invalid, go through the OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh the token if expired and refresh token is available
            creds.refresh(Request())
        else:
            # Go through OAuth flow to get new credentials
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=8005, access_type='offline', prompt='consent')

        # Save the new credentials to token.json for future use
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())

    return creds
