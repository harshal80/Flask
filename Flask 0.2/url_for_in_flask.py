from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def welcome():
    return " Hi harshal "


@app.route("/student")
def student():
    return "welcome student "


@app.route("/fac")
def fac():
    return "welcome faculty "


@app.route("/user/<name>")
def user(name):
    if name == "student":
        return redirect(url_for("student"))
    if name == "fac":
        return redirect(url_for("fac"))


app.run(debug=True)
