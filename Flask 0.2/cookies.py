from flask import Flask, render_template, make_response, request

app = Flask(__name__)


@app.route("/set")
def setcookis():
    res = make_response("<h1> Cookie is set</h1>")
    res.set_cookie("framework", "flask")
    return res


@app.route("/get")
def getcookie():
    name = request.cookies.get("framework")
    return name


@app.route("/")
def index():
    count = int(request.cookies.get("visited_count", 0))
    count += 1
    msg = "visited this page " + str(count)
    resp = make_response(msg)
    resp.set_cookie("visited_count", str(count))
    return resp


app.run(debug=True)
