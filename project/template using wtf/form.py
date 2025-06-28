from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField,IntegerField,DecimalField,SelectField,RadioField,FileField,TextAreaField,SubmitField
from wtforms.validators import InputRequired

#objectives
# 1.) take the name of name
# 2.) take their aadhar no.
# 3.) take password
# 4.) take their age
# 5.) take their salary expectations
# 6.) take their location
#             SUBMIT

class PassportForms(FlaskForm):
    name = StringField("Enter your name : ",validators=[InputRequired()])
    aadhar = IntegerField("Enter your aadhar no : ",validators=[InputRequired()])
    age = IntegerField("Enter your age : ",validators=[InputRequired()])
    password = PasswordField("Set a strong password",validators=[InputRequired()])
    salary = DecimalField("Enter your salary (from past 1 year) : ", validators=[InputRequired()])
    gender = RadioField("Gender",choices=[("M","Male"),("F","Female"),("NA","Rather not to say")],validators=[InputRequired()])
    location = SelectField("location", choices=[("ND", "new delhi"),("BN","Banglore"),("MB","Mumbai")],validators=[InputRequired()])
    info = BooleanField("Inform via Email")
    photo = FileField("Photo",validators=[InputRequired()])
    feedback = TextAreaField("Give your feedback")