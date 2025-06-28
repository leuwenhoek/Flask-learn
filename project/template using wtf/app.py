from flask import Flask,render_template,session,url_for,redirect,request
import form

app = Flask(__name__)
app.config['SECRET_KEY'] = "don't tell anyone"

@app.route("/",methods=["GET","POST"])
def render():
    forms = form.PassportForms()
    if forms.validate_on_submit():
         session["form_data"] = {
            "name" : forms.name.data,
            'aadhar' : forms.aadhar.data,
            'age' : forms.age.data,
            'password' : forms.password.data,
            'salary' : forms.salary.data,
            'gender' : forms.gender.data,
            'location' : forms.location.data,
            'info' : forms.info.data,
            'photo' : forms.photo.data.filename,
            'feedback' : forms.feedback.data,
         }
         return redirect(url_for("verify_it"))
    return render_template("index.html",form=forms)

@app.route("/success")
def done():
    return "Thanks for giving your details"

@app.route("/verify")
def verify_it():
    data = session.get('form_data')
    return render_template("verify.html", data=data)
if __name__ == '__main__':
    app.run()