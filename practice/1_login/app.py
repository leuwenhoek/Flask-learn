from flask import Flask,session,request,url_for,redirect, render_template
import form

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/",methods=["GET","POST"])
def main():
    if request.method == "POST":
        answer = request.form.get("answer")
        if answer == "yes":
            return render_template("greet.html")
        elif answer == "no":
            return redirect(url_for("create_email"))
        else: 
            return f"<h1>Invalid submition<h1>"
    return render_template("is_logined.html")

@app.route("/create",methods=["GET","POST"])
def create_email():
    myform = form.login()
    if myform.validate_on_submit():
        session["data"] = {
            "fname": myform.fname.data,
            "lname": myform.lname.data,
            "mob": myform.mob.data,
            "is_paid": myform.is_paid.data,
            "email": myform.email.data,
            "password": myform.password.data,
        }
        return redirect(url_for("veri"))
    return render_template("index.html",form=myform)

@app.route("/verify", methods=["GET","POST"])
def veri():
    data = session.get("data")
    return render_template("verify.html",data=data)

if __name__ == '__main__':
    app.run()
