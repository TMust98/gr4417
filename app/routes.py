from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    username = "Timur"
    return render_template("index.html", username=username)