import random
import plotly.express as px
import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()
DOCUMENT_ID = os.getenv("GOOGLE_SHEET_ID", default="OOPS")
SHEET_NAME = os.getenv("SHEET_NAME", default="Responses")


#Defining essential lists and functions
clubList = ["Abigail", "Sign of the Whale", "Tokyo Pearl", "Ultrabar", "Decades"]
yearList = ["Freshman", "Sophomore", "Junior", "Senior"]
entries = []

def generateEntries(length):
    x = 0
    while x < length:
        club = random.choice(clubList)
        year = random.choice(yearList)
        addEntry([club, year])
        x += 1

def authorizeGoogleSheets():
    CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "google-credentials.json")

    AUTH_SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
        "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
    client = gspread.authorize(credentials)
    return client

def readEntries():
    # access the document:
    client = authorizeGoogleSheets()
    doc = client.open_by_key(DOCUMENT_ID)

    # access a sheet within the document:
    sheet = doc.worksheet(SHEET_NAME)

    # fetch all data from that sheet:
    rows = sheet.get_all_records()
    return rows

def addEntry(entry) :
    if (len(entry) != 2):
        raise Exception("Incorrect entry syntax in addEntry")

    client = authorizeGoogleSheets()
    doc = client.open_by_key(DOCUMENT_ID)
    sheet = doc.worksheet(SHEET_NAME)
    rows = sheet.get_all_records()
    newRow = {"Club": entry[0], "Year": entry[1]}

    new_values = list(newRow.values())

    next_row_number = len(rows) + 2

    response = sheet.insert_row(new_values, next_row_number)

#def generateChartData():


if __name__ == "__main__":
    #generateEntries(10)

    #Generating output graphics
    clubFrequency = [0, 0, 0, 0, 0]

    symbol = "ALL" # @param ["ALL", "Freshman", "Sophomore", "Junior", "Senior"]
    if (symbol == "ALL"):
        for entry in entries:
            idx = clubList.index(entry["club"])
            clubFrequency[idx] = clubFrequency[idx] + 1
    else:
        for entry in entries:
            if (entry["year"] == symbol):
                idx = clubList.index(entry["club"])
                clubFrequency[idx] = clubFrequency[idx] + 1

    fig = px.bar(x=clubList, y=clubFrequency, labels={"y": "Frequency", "x": "Club"})
    #fig.show()
