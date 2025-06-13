from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def studentinfo():
    return render_template(
        "index.html",
        name = "amit",
        is_topper = True,
        subjects = {"maths" : 90, "science" : 90, "english" :90}
                           )