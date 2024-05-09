from flask import Flask, request, render_template, session

app = Flask(__name__)

app.secret_key = "loginform"


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def login1():
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("password")
        if user == "harshal" and password == "123":
            session["email"] = user
            return render_template("successes.html", email=user)
        else:
            msg = "Invalid username or passwordf"
            return render_template("login.html", msg=msg)
    else:
        user = request.form.get("user")
        password = request.form.get("password")
        if user == "harshal" and password == "123":
            session["email"] = user
            return render_template("successes.html", email=user)
        else:
            msg = "Invalid username or password"
            return render_template("login.html", msg=msg)


@app.route("/logout")
def logout():
    session.pop("email", None)
    return render_template("login.html")


app.run(debug=True)
