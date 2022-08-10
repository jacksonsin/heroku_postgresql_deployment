from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<aws resources>'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'password'

db = SQLAlchemy(app)

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    eid = db.Column(db.String(120), nullable=False)

    def __init__(self, name, eid):
        self.name = name
        self.eid = eid

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/personadd", methods=['POST'])
def personadd():
    name = request.form["name"]
    eid = request.form["eid"]
    entry = People(name, eid)
    db.session.add(entry)
    db.session.commit()
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = False
    db.create_all()
    app.run()
