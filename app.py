import os
from flask import Flask, render_template, redirect, url_for
from forms import FormLogin, FormRegister
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", title="Home Page")


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
        return redirect(url_for("user_login"))
    return render_template(
        "user-registration.html", title="Sign Up", form=form)


@app.route('/recipe-editor')
def recipe_editor():
    return render_template("recipe-editor.html", title="Recipe Editor")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
