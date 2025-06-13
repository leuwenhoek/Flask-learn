from flask import Flask
from flask import request,redirect,url_for,session,Response

app = Flask(__name__)
app.secret_key="secret"

@app.route("/", methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        mobile_no = request.form.get("Mobile")
        password = request.form.get("password")

        if username == "Ayush" and password == "123" and mobile_no == "0000":
            session["user"] = username
            return redirect(url_for("welcome_user"))
        else:
            return Response("invalid details. try again later", mimetype="text/plain") #return plain text (by default it sends HTML)
        
    return """
    <h1>Login page</h1>
    <span><h5>This is my first login page using flask</h5></span><br>

    <form method="POST">
    <label for="username"><b>Username: </b></label>
    <input type="text" placeholder="username" name="username" required><br>

    <label for="mobile"><b>Mobile no: </b></label>
    <input type="text" placeholder="Mobile no" name="Mobile" required><br>

    <label for="pass"><b>Password: </b></label>
    <input type="Password" placeholder="password" name="password" required><br>

    <input type="submit" value="login">
    </form>

    """

@app.route("/welcome")
def welcome_user():
    if "user" in session:
        return f"""
            <h1>welcome {session["user"]}</h1>
            <br>
            <p><b><i>Content coming soon</i></b></p>
            <a href="{url_for("logout")}">Logout</a>
        """
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.secret_key = "secret"
    app.run(debug=True)

