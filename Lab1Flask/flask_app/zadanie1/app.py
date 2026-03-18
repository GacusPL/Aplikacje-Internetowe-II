from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
    
#zad3
@app.route("/o-nas")
def about():
    return "<p>Kacper Szponar 21306</p><p>To jest aplikacja testowa z laboratorium 1.</p>"

@app.route("/user/<name>")
def show_user(name):
    return f"Witaj, {name}!"