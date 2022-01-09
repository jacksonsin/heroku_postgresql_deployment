from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hnnwinwflpkjdq:2f0721a5d89894008beb0299136fd7acfa1e016815135bc94adfd1b274056c97@ec2-54-221-82-166.compute-1.amazonaws.com:5432/d94p3l6dfsa1ob'
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
def addperson():
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
