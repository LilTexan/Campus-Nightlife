# Campus-Nightlife
##Web-Based Use
Python-based web application that compiles and displays data on where Georgetown students are going out.
Deployed using Render, the site can be found [here](https://georgetown-nightlife.onrender.com).

##Local Use
### Setting Up a Virtual Environment
Create your virtual environment:
```
conda create -n nightlife-env python=3.8
```
Activate your virtual environment:
```
conda activate nightlife-env
```
Install necessary packages for the program:
```
pip install -r requirements.txt
```

### Configuration
Obtain an API Key from Google: [Click Here](https://console.cloud.google.com/)
Next, download the required JSON file, name it google-credentials.json, and place it in a folder titled "auth" within the "app" folder:
```
/Campus-Nightlife/app/auth/google-credentials.json
```
Additionally, you will need to create a google sheet to store the data for the site. Create a sheet, share it with your service account, and update the .env file to include the following fields:
```
GOOGLE_SHEET_ID="Your Sheet ID Here"
SHEET_NAME="Your Sheet Name Here"
```
Once this is done, create columns in your Google Sheets file titled (in order): [Club, Year]


### Usage
Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```
