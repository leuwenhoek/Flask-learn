from flask import Flask 
from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,PasswordField,IntegerField,BooleanField
from wtforms import validators
from wtforms.validators import InputRequired

class login(FlaskForm):
    fname = StringField("Enter your first name : ",validators=[InputRequired()])
    lname = StringField("Enter your last name : ",validators=[InputRequired()])
    mob = IntegerField("Enter your mobile number : ",validators=[InputRequired()])
    is_paid = BooleanField("do you want premium features in your email ?")
    email = EmailField("Enter the email you want : ",validators=[InputRequired()])
    password = PasswordField("Set a strong password : ", validators=[InputRequired()])
