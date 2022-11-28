import random
import plotly.express as px

#Defining essential lists and functions
clubList = ["Abigail", "Sign of the Whale", "Tokyo Pearl", "Ultrabar", "Decades"]
yearList = ["Freshman", "Sophomore", "Junior", "Senior"]
entries = []

def addEntry (entry):
    if (len(entry) != 2):
        raise Exception("Incorrect entry syntax in addEntry")
    entries.append({"club": entry[0], "year": entry[1]})


if __name__ == "__main__":
    #Generating randomized entries
    x = 0
    while x < 50:
        club = random.choice(clubList)
        year = random.choice(yearList)
        addEntry([club, year])
        x += 1

    print(entries)

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
