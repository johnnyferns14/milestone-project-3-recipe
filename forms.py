from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
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
