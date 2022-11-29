import random
import plotly.express as px
import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

#Defining essential lists and functions
clubList = ["Abigail", "Sign of the Whale", "Tokyo Pearl", "Ultrabar", "Decades"]
yearList = ["Freshman", "Sophomore", "Junior", "Senior"]
entries = []

def addEntry (entry):
    if (len(entry) != 2):
        raise Exception("Incorrect entry syntax in addEntry")
    entries.append({"club": entry[0], "year": entry[1]})

def generateEntries(length):
    x = 0
    while x < length:
        club = random.choice(clubList)
        year = random.choice(yearList)
        addEntry([club, year])
        x += 1

#Working with Google Sheets
def authorizeGoogleSheets():
    DOCUMENT_ID = os.getenv("GOOGLE_SHEET_ID", default="OOPS")
    SHEET_NAME = os.getenv("SHEET_NAME", default="Responses")

    CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "google-credentials.json")

    AUTH_SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
        "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
    print("CREDS:", type(credentials)) #> <class 'oauth2client.service_account.ServiceAccountCredentials'>

    client = gspread.authorize(credentials)
    print("CLIENT:", type(client)) #> <class 'gspread.client.Client'>

    print("-----------------")
    print("READING DOCUMENT...")

    # access the document:
    doc = client.open_by_key(DOCUMENT_ID)
    print("DOC:", type(doc), doc.title) #> <class 'gspread.models.Spreadsheet'>

    # access a sheet within the document:
    sheet = doc.worksheet(SHEET_NAME)
    print("SHEET:", type(sheet), sheet.title)#> <class 'gspread.models.Worksheet'>

    # fetch all data from that sheet:
    rows = sheet.get_all_records()
    print("ROWS:", type(rows)) #> <class 'list'>

    # loop through and print each row, one at a time:
    for row in rows:
        print(row) #> <class 'dict'>

if __name__ == "__main__":
    generateEntries(50)
    authorizeGoogleSheets()

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
    fig.show()
