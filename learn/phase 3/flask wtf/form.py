from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,SubmitField
from wtforms.validators import DataRequired,Email,length

class Registrationform(FlaskForm):
    name= StringField("Full name", validators=DataRequired())
    email= StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired(),length(min=5)])
    submit=SubmitField("Register")