import os
from flask import (
    Flask, render_template,
    redirect, url_for, flash, request, session)
from forms import FormLogin, FormRegister, FormRecipe
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
    recipies = mongo.db.recipies.find()
    return render_template(
        "index.html", title="Home Page", members=members, recipies=recipies)


@app.route('/about')
def about():
    return render_template("about.html", title="About Us")


@app.route('/user-login', methods=["POST", "GET"])
def user_login():
    form = FormLogin()
    if form.validate_on_submit():
        if request.method == "POST":
            member_exists = mongo.db.members.find_one(
                {"email": request.form.get("email").lower()})

            if member_exists:
                if check_password_hash(
                        member_exists["password"], request.form.get(
                            "password")):
                    session["member"] = request.form.get("email").lower()
                    flash("Welcome {}, You are logged in." .format(
                        request.form.get("email")))
                    return redirect(url_for(
                        "dashboard", email=session["member"]))
                else:
                    flash("Invalid email/password combination")
                    return redirect(url_for("user_login"))
            else:
                flash("Invalid email/password combination")
                return redirect(url_for("user_login"))
    return render_template("user-login.html", title="Login Page", form=form)


@app.route('/user-registration', methods=["POST", "GET"])
def user_registration():
    form = FormRegister()
    if form.validate_on_submit():
        if request.method == "POST":
            member_exists = mongo.db.members.find_one(
                {"email": request.form.get("email").lower()})
            if member_exists:
                flash("User with same email id already exists")
                return redirect(url_for("user_registration"))
            member_info = {
                "name": request.form.get("name").lower(),
                "email": request.form.get("email").lower(),
                "password": generate_password_hash(request.form.get(
                    "password"))
            }
            mongo.db.members.insert_one(member_info)

            session["member"] = request.form.get("email").lower()
            flash("User registered successfully")
            return redirect(url_for("dashboard", email=session["member"]))
    return render_template(
        "user-registration.html", title="Sign Up", form=form)


@app.route('/dashboard')
def dashboard():
    email = mongo.db.members.find_one(
        {"email": session["member"]})["email"]
    return render_template("dashboard.html", title="Dashboard", email=email)


@app.route('/my-recipes')
def my_recipes():
    mongo.db.recipies.find({session["member"]})
    return render_template("my-recipes.html", title="My Recipes")


@app.route('/recipe-editor', methods=["POST", "GET"])
def recipe_editor():
    form = FormRecipe()
    if form.validate_on_submit():
        if request.method == "POST":

            recipe_info = {
                "title": request.form.get("title"),
                "description": request.form.get("description"),
                "category": request.form.get("category"),
                "image_url": request.form.get("image_url"),
                "ingredients": request.form.get("ingredients").splitlines(),
                "directions": request.form.get("directions").splitlines(),
                "contributor": session["member"]

            }
            mongo.db.recipies.insert_one(recipe_info)
            flash("Your recipe was successfully added.")
        return redirect(url_for("index"))
    return render_template(
        "recipe-editor.html", title="Recipe Editor", form=form)


@app.route('/edit-recipe/<recipe_id>', methods=["GET", "POST"])
def edit_recipe(recipe_id):
    form = FormRecipe
    if form.validate_on_submit():
        if request.method == "POST":

            recipe_info = {
                "title": request.form.get("title"),
                "description": request.form.get("description"),
                "category": request.form.get("category"),
                "image_url": request.form.get("image_url"),
                "ingredients": request.form.get("ingredients").splitlines(),
                "directions": request.form.get("directions").splitlines(),
                "contributor": session["member"]

            }
            mongo.db.recipies.update_one(
                {"_id": ObjectId(recipe_id)}, recipe_info)
            flash("Your recipe was successfully updated.")
    recipe = mongo.db.recipies.find_one(
        {"_id": ObjectId(recipe_id)})

    return render_template(
        "edit-recipe.html", title="Recipe Editor", recipe=recipe)


@app.route('/delete-recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipies.remove(
        {"_id": ObjectId(recipe_id)})
    flash("Your recipe was successfully deleted.")
    return redirect(url_for("index"))


@app.route('/logout')
def logout():
    flash("Logged out!")
    session.pop("member")
    return redirect(url_for("user_login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
