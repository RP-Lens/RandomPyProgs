from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "OliverSmelly"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def index():
    return render_template("index.html", stuff=["jim", "joe", "bill"])

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form['nm']
        session["user"] = user

        foundUser =  users.query.filter_by(name=user).first()
        if foundUser:
            session["email"] = foundUser.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash("u got logged inned", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("ur already logged inned stoopid", "info")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route('/user', methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            foundUser =  users.query.filter_by(name=user).first()
            foundUser.email = email
            db.session.commit()
            flash("email saved lol get rekt newb")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
    else:
        flash("u arnet logged in stoopid", "info")
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    flash("you got logged outed", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)