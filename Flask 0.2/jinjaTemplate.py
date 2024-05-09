from flask import Flask, render_template

app = Flask(__name__)


# Delimiters:
# Types of Delimiters:
# 1) { { value } }:-that can use to simple print of display values or variable or expration on html page
# 2) {% ... %} :-it can use to control statement if else for , ....
# 3){# value #} :- it use to set comment on value or variable
@app.route("/")
def hello():
    dict = {"maths": 99, "Science": 89, "programing": 99}
    return render_template("msg.html", result=dict, name="harshal")


@app.route("/<uname>")  # passing name
def hellonaem(uname):
    return render_template("msg.html", name=uname)


app.run(debug=True)
