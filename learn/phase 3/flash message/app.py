from flask import Flask,render_template,redirect,url_for,request,flash

app=Flask(__name__)
app.secret_key = "secret"

@app.route("/",methods=["GET","POST"])
def form():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        if not name:
            flash("name is empty")
            return redirect(url_for("form"))
        elif not password:
            flash("Pasword is empty")
            return redirect(url_for("form"))
        flash(f"Thanks {name}, your details are saved")
        return redirect(url_for("form"))
    return render_template("login.html")