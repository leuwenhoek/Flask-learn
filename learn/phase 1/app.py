from flask import Flask
from flask import request

#creating a application using flask

app=Flask(__name__)  #created a object that represents our website

@app.route("/home") #tell flask that it should show the user all the info written below (on the page "/home")
def show():
    return "hello user"

@app.route("/about")
def about():
    return "my name is Ayush"

@app.route("/contactus")
def contact():
    return "mobile no. - XXXXX-XXXXX"

@app.route("/submit", methods=["GET","POST"])
def user():
    if request.method == "POST":
        return "data has been sent!!"
    else:
        return "hlo visitor"
        