from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/page")
def msg():
    return "hello"


app.run(debug=True)
