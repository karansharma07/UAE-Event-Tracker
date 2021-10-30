from flask import Flask, flash, jsonify, redirect, render_template, request, session, send_from_directory
from flask_session import Session
from tempfile import mkdtemp

from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events",
    headers={
      "Authorization": "Bearer kVMmdcgMaADgkybSkDoFAqVWLBxiEofIRRbdNFNt",
      "Accept": "application/json"
    },
    params= {
    "active.gte": "2019-12-29",
    "active.lte": "2021-01-10",
        "country" : "AE"
    }
)

print(response.json())

# Configure application
app = Flask(__name__)

# you can set key as config
# app.config['GOOGLEMAPS_KEY'] = "AIzaSyB0PDmZAbO-kymDmu61za81KLh5rtufGAo"

# Initialize the extension
# GoogleMaps(app)

# you can also pass the key here if you prefer
GoogleMaps(app, key="AIzaSyBeXr8TNLiXFga7Ja69_MHHEak2Ng6kECE")


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



     # redirect("/")


@app.route("/")
def index():
    # creating a map in the view
    locations = []
    result = response.json()

    for result in result['results']:
        loc = result['location']
        loc.append(result['title'])
        locations.append(loc)

    markers=[(loc[1], loc[0], loc[2]) for loc in locations]
    print(markers, flush = True)
    mymap = Map(
        identifier="view-side",
        markers=[(loc[1], loc[0]) for loc in locations],
        lat=locations[0][1],
        lng=locations[0][0]
    )

    print(mymap, flush = True)

    return render_template('index.html', mymap=mymap, lat = locations[0][1], lng = locations[0][0],
    len = len(markers), markers = markers)



if __name__ == '__main__':
    app.run()
