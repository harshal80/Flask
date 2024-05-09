from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = " login form "


@app.route("/")
def sss():
    return render_template("form2.html")


@app.route("/formlogin", methods=["GET"])  # get method
def login():
    error = None
    user = request.args.get("user")
    password = request.args.get("password")
    if user == "harshal" and password == "123":
        flash("you are successully login")
        return render_template("mes2.html", name="user")
    else:
        error = "invalid username and password"
        return redirect(url_for("form2.html", error1=error))


# @app.route("/formlogin", methods=["POST"])  # post method
# def login():
#     user = request.form["user"]
#     password = request.form["password"]
#     if user == "harshal" and password == "123":
#         return "welcome %s" % user
#     else:
#         return "invalid data "


app.run(debug=True)
