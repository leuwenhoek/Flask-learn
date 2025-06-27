from form import Registrationform
from flask import Flask,flash

app=Flask(__name__)

@app.route("/")
def register():
    form = Registrationform()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Thank you {name}, for submitting registration form")