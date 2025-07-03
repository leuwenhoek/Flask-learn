from flask import Flask,redirect,render_template,request,url_for,session,sessions,flash
import os
import sqlite3

app = Flask(__name__)
app.secret_key = "GET_OUT_OF HERE_YOU-DUMB_HACKER"
app.config["SESSION_TYPE"] = "filesystem"

def path(name):
    path2 = os.path.join("project","placing order",name)
    return path2
    
def initialize_buyerdb():
    path2 = os.path.join("project","placing order","database.db")
    conn = sqlite3.connect(path2)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS buyers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            store TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            mobile_number INTEGER NOT NULL,
            username TEXT UNIQUE not null,
            password TEXT UNIQUE NOT NULL

        )
''') 
    
    conn.commit()
    conn.close()

def initialize_orderdb():
    path2 = os.path.join("project","placing order","order.db")
    conn = sqlite3.connect(path2)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            books TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert(val1, val2, val3, val4, val5, val6):
    conn = sqlite3.connect(path("database.db"))
    curr = conn.cursor()
    curr.execute(
        "INSERT INTO buyers (name, store, email, mobile_number, username, password) VALUES (?, ?, ?, ?, ?, ?)",
        (val1, val2, val3, val4, val5, val6)
    )
    conn.commit()
    conn.close()

def save_order(username,items):
    conn = sqlite3.connect(path("order.db"))
    curr = conn.cursor()
    curr.execute(
        "INSERT INTO buyers (username,books) VALUES (?, ?)",
        (username,items)
    )
    conn.commit()
    conn.close()

def fetch(username,password):
    conn = sqlite3.connect(path("database.db"))
    curr = conn.cursor()
    curr.execute('SELECT * FROM buyers WHERE username=? AND password=?',(username,password))
    user = curr.fetchall()
    conn.commit()
    conn.close()

    return user

def get_session_data():
    name = session.get("name")
    store = session.get("store")
    email = session.get("email")
    mobile = session.get("mobile")
    username = session.get("username")

    return name,store,email,mobile,username

@app.route("/")
def home():
    return redirect(url_for("log"))

@app.route("/login", methods=["POST", "GET"])
def log():
    if request.method == "POST":
        username = request.form.get("name")
        password = request.form.get("password")
        user = fetch(username, password)
        if user:
            session["name"] = username
            session["password"] = password
            return redirect(url_for("wel"))
        else:
            flash("Invalid username or password!", "danger")
            return render_template("login.html")
    return render_template("login.html")


@app.route("/signup", methods=["POST", "GET"])
def sign():
    if request.method == "POST":
        session["name"] = name = request.form.get("name")
        session["store"] = store = request.form.get("store")
        session["email"] = email = request.form.get("email")
        session["mobile"] = mobile = request.form.get("mobile")
        session["username"] = username = request.form.get("username")
        session["password"] = password = request.form.get("password")
        try:
            insert(name, store, email, mobile, username, password)
            return redirect(url_for("wel"))
        except sqlite3.IntegrityError as e:
            return render_template("signup.html", error="Email, username, or mobile already exists!")
    return render_template("signup.html")

@app.route("/home",methods=["POST","GET"])
def wel():
    name,store,email,mobile,username = get_session_data()
    if request.method == "POST":
        selected_books = []
        selected_books = request.form.getlist("books")
        session["books"] = selected_books 
        session["cost"] = len(selected_books) * 500
        return redirect("/buy")
    return render_template("home.html",name=name,store=store,email=email,username=username)

@app.route("/buy", methods=["POST", "GET"])
def cart():
    selected_books_ = session.get("books",[])
    if request.method == "POST":
        save_order(session.get("username"),items=selected_books_)
    cost = session.get("cost",0)
    cost_ = len(selected_books_)*500
    session["cost"] = cost_
    return render_template("complete_order.html",selected_books=selected_books_, cost = cost_ )
if __name__ == "__main__":
    initialize_buyerdb()
    initialize_orderdb()
    app.run(debug=True)