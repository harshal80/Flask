from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def reg():
    return render_template("formfile.html")


@app.route("/susss", methods=["POST"])
def printdata():
    f = request.files["file"]
    f.save("static/" + f.filename)
    return "sussecss"


app.run(debug=True)
