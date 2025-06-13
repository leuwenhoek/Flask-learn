from flask import Flask,render_template,url_for,redirect,request

app=Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "Ayush" and password == "123":
            return redirect(url_for("wel"))
        else:
            return "Invalid details"
    return render_template("form.html")

@app.route("/welcome")
def wel():
    return render_template("welcome.html")