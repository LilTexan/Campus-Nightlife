
# this is the "web_app/routes/stocks_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

from app.entries import readEntries, addEntry, countFrequencies, returnClubs, returnYears

nightlife_routes = Blueprint("nightlife_routes", __name__)

@nightlife_routes.route("/")
@nightlife_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("home.html")

@nightlife_routes.route("/form")
def form():
    print("NIGHTLIFE FORM...")
    return render_template("form.html")

@nightlife_routes.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    print("NIGHTLIFE DASHBOARD...")
    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
        #breakpoint()
        addEntry([request.form["Club"], request.form["Year"]])
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    #symbol = request_data.get("symbol") or "NFLX"

    try:
        #df = fetch_stocks_data(symbol=symbol)
        #latest_close_usd = format_usd(df.iloc[0]["adjusted_close"])
        #latest_date = df.iloc[0]["timestamp"]
        #data = df.to_dict("records")

        entries = readEntries()
        frequencies = countFrequencies(entries)
        freshmanFrequencies = countFrequencies(entries, "Freshman")
        sophomoreFrequencies = countFrequencies(entries, "Sophomore")
        juniorFrequencies = countFrequencies(entries, "Junior")
        seniorFrequencies = countFrequencies(entries, "Senior")
        clubList = returnClubs()
        yearList = returnYears()

        #flash("Fetched Real-time Market Data!", "success")
        return render_template("dashboard.html",
            entries=entries,
            frequencies=frequencies,
            freshmanFrequencies=freshmanFrequencies,
            sophomoreFrequencies=sophomoreFrequencies,
            juniorFrequencies=juniorFrequencies,
            seniorFrequencies=seniorFrequencies,
            clubList=clubList,
            yearList=yearList
        )
    except Exception as err:
        print('OOPS', err)

        #flash("Market Data Error. Please check your symbol and try again!", "danger")
        return redirect("/form")
