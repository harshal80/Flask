from flask import Flask  # flask libreay to import Flask class

app = Flask(__name__)  # simpley Flask class object can create : app


@app.route("/")
def hello():
    return "hello world"


@app.route("/harshal")
def harsh():
    return "hello Harshal I am backend devloper "


app.run(
    debug=True
)  # debug =True is simply you can change the code your webpage also cange
