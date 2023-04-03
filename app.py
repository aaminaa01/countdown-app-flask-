from flask import Flask
from flask import render_template
from datetime import datetime
app = Flask(__name__)
@app.route("/")
def countdown():

    launchTime = datetime(2023, 10, 5)
    currentTime = datetime.now()
    diff = launchTime - currentTime
    numberOfMilliseconds = int(diff.total_seconds() * 1000)

    return render_template(
        "countdown.html",
        time=numberOfMilliseconds
    )