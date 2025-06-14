from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",page="home")

@app.route("/about")
def about():
    return render_template("index.html", page="about us")

@app.route("/products")
def product():
    return render_template("index.html", page="products")

@app.route("/contact")
def contact():
    return render_template("index.html", page="contact us")