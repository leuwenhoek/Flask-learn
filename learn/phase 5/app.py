import sqlite3
from flask import Flask,render_template,request,redirect,url_for

DB_PATH = 'learn/phase 5/database.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()                                     #pointer that executes all the functions inside the given db
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
    )
    ''')

    conn.commit()
    conn.close()


app = Flask(__name__)
@app.route("/")
def home():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    conn.close()
    return render_template("home.html",users=users)

@app.route("/add",methods=["POST"])
def add_user():
    name = request.form["name"]
    email = request.form["email"]

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (?, ?)",(name,email))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
    app.run()