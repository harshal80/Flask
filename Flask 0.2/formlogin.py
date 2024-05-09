from flask import Flask, request

app = Flask(__name__)


# @app.route("/formlogin", methods=["GET"])  # get method
# def login():
#     user = request.args.get("user")
#     password = request.args.get("password")
#     if user == "harshal" and password == "123":
#         return "welcome %s" % user
#     else:
#         return "invalid data "


@app.route("/formlogin", methods=["POST"])  # post method
def login():
    user = request.form["user"]
    password = request.form["password"]
    if user == "harshal" and password == "123":
        return "welcome %s" % user
    else:
        return "invalid data "


app.run(debug=True)
