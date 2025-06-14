from flask import Flask,render_template,url_for,redirect,request

app=Flask(__name__)

@app.route("/")
def default():
    return redirect(url_for("home"))

@app.route("/Home", methods=["GET","POST"])
def home():
    if request.method=="POST":
        name = request.form.get("name","guest")
        return render_template("greet.html",name=name)
    else:
        return render_template("index.html")
    