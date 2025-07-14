from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def show():
    if request.method == "POST":
        answer = request.form.get("answer")
        if answer=="yes":
            return redirect(url_for("yes"))
        elif answer=="no":
            return redirect(url_for("no"))
    
    return render_template("index.html")
    
@app.route("/Iknow")
def yes():
    return render_template("i_knew_it.html",message="then, just upvote bro... 🙂")

@app.route("/chalna")
def no():
    return render_template("index.html",message="Enter again", no=True)

if __name__ == "__main__":
    app.run(debug=True)