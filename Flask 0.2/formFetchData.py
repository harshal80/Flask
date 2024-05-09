from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def reg():
    return render_template("formFetch.html")


@app.route("/suss", methods=["POST"])
def printdata():
    result = request.form

    return render_template("result.html", result2=result)


app.run(debug=True)
