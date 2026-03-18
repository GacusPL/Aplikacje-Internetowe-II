from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hobby")
def hobby():
    return render_template("hobby.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")