from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/harshal")
def harsh():
    return "hello Harshal I am backend devloper "


app.run(debug=True)
