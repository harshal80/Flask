from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"


# @app.route("/<name>")  # passing name
# def hellonaem(name):
#     return "hello " + name


@app.route("/<int:date>")
def hello_harsh(date):
    return "date=%d" % date


app.run(debug=True)
