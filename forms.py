from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class FormRegister(FlaskForm):
    name = StringField("Full Name", validators=[
                       DataRequired(), Length(min=3, max=30)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=6)])
    confirm_password = PasswordField(
        "Confirm Password", validators=[EqualTo("password")])
    submit = SubmitField("Sign Up")


class FormLogin(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=6)])
    submit = SubmitField("Login")


class FormRecipe(FlaskForm):
    title = StringField(
        "Recipe Title", validators=[DataRequired(), Length(min=5, max=20)])
    description = TextAreaField(
        "Description", validators=[DataRequired(), Length(min=40)])
    category = TextAreaField(
        "Category", validators=[DataRequired(), Length(min=5)])
    image_url = StringField(
        "Image URL", validators=[DataRequired(), Length(min=15)])
    ingredients = TextAreaField(
        "Ingredients", validators=[DataRequired(), Length(min=15)])
    directions = TextAreaField(
        "Directions", validators=[DataRequired(), Length(min=15)])
    save_recipe = SubmitField("save")
