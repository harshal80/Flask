from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/mydb"
app.config["SQLALCHEMY_MODUFICATIONS"] = True
db = SQLAlchemy(app)


class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gmail = db.Column(db.String(120), nullable=False)  #


@app.route("/")
def index():
    fname = "Harshal"
    email = "harsahl@gamil.com"
    entry = Contact(
        name=fname,
        gmail=email,
    )
    db.session.add(entry)
    db.session.commit()
    return "succesful"


app.run(debug=True)
