from flask import Flask,redirect,render_template,request,url_for
import sqlite3

app = Flask(__name__)
PATH = "project\creating account and saving in db\database.db"

def initialize_db():
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS accounts(
                    id  INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    username TEXT UNIQUE NOT NULL,
                    mobile_no INTEGER UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT UNIQUE NOT NULL
                )
    ''')

    conn.commit()
    conn.close()

@app.route("/",methods=["POST","GET"])
def send_user():
    want = request.form.get("want")
    if want == "LOGIN":
        return redirect(url_for("login"))
    elif want == "SIGNUP":
        return redirect(url_for("signup"))
    return render_template("home.html")

@app.route("/login",methods=["POST","GET"])
def login():
        if request.method == "POST":
             email = request.form.get("email")
             password = request.form.get("password")

             conn = sqlite3.connect(PATH)
             cur = conn.cursor()

             cur.execute("SELECT * FROM accounts WHERE email=? AND password=?",(email,password))
             user = cur.fetchone()

             conn.close()

             if user:
                return redirect(url_for("done",message="code2"))
             else:
                return render_template("login.html",status="check your details again")
        return render_template("login.html")

@app.route("/signup",methods=["POST","GET"])
def signup():
    if request.method == "POST":
        fname = request.form.get("fname")
        username = request.form.get("username")
        lname = request.form.get("lname")
        mob = request.form.get("mob")
        email = request.form.get("email")
        password = request.form.get("password")

        conn= sqlite3.connect(PATH)
        cur = conn.cursor()
        cur.execute("INSERT INTO accounts(first_name,last_name,username,mobile_no,email,password) VALUES(?,?,?,?,?,?)", (fname,lname,username,mob,email,password))
        conn.commit()
        conn.close()
        return redirect(url_for("done",message="code1"))
    return render_template("signup.html")

@app.route("/success")
def done():
     message = request.args.get("message")
     if message == "code1":
          return render_template("success.html",info="account has been created")
     elif message == "code2":
          return render_template("success.html",info="successfully logined")
     else:
          return render_template("error.html")
if __name__ == "__main__":
    initialize_db()
    app.run(debug=True)