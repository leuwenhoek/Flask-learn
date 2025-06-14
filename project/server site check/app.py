from flask import Flask,request,redirect,render_template,url_for,session

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def render():
    return render_template("index.html")

@app.route("/register",methods=["POST"])
def check():
    username = request.form.get("name", "Guest")
    if not request.form.get("name") and request.form.get("DOB") and request.form.get("sports") and request.form.get("Email"):
        return render_template("status.html", status="Fail, try again")
    
    else:
        return render_template("status.html", status=f"Thanks {username} for giving your info.")