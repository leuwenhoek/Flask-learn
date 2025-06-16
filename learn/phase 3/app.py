from flask import Flask,request,render_template,redirect,url_for

app=Flask(__name__)


@app.route("/")
def send():
    return redirect(url_for("feedback"))

@app.route("/feedback",methods=["GET","POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        message_ = request.form.get("message")

        return render_template("thankyou.html", user=name, message=message_)
    
    return render_template("feedback.html")
