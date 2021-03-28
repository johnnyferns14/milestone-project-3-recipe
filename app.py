import os
from flask import (
    Flask, render_template,
    redirect, url_for, flash, request, session)
from forms import FormLogin, FormRegister
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def index():
    members = mongo.db.members.find()
    return render_template("index.html", title="Home Page", members=members)


@app.route('/about')
def about():
    return render_template("about.html", title="About Us")


@app.route('/user-login', methods=["POST", "GET"])
def user_login():
    form = FormLogin()
    if form.validate_on_submit():
        return redirect(url_for("index"))
    return render_template("user-login.html", title="Login Page", form=form)


@app.route('/user-registration', methods=["POST", "GET"])
def user_registration():
    form = FormRegister()
    if form.validate_on_submit():
        if request.method == "POST":
            member_exists = mongo.db.members.find(
                {"email": request.form.get("email").lower()})
            if member_exists:
                flash("User with same email id already exists")
                return redirect(url_for("user_registration"))
            member_info = {
                "name": request.form.get("name").lower(),
                "email": request.form.get("email").lower(),
                "password": generate_password_hash(request.form.get("password"))
            }

    #     return redirect(url_for("user_login"))
    return render_template(
        "user-registration.html", title="Sign Up", form=form)


@app.route('/recipe-editor')
def recipe_editor():
    return render_template("recipe-editor.html", title="Recipe Editor")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
