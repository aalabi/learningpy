import datetime
from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    headline = "Hello World"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "GoodBye"
    return render_template("index.html", headline=headline)

@app.route("/list")
def list():
    names = {"Alabi", "Benedict", "Opeyemi", "Jonathan", 'Rosemary'}
    return render_template("list.html", names=names)

@app.route("/new-year")
def new_year():
    now = datetime.datetime.now()
    newYear = now.month == 1 and now.day == 1
    return render_template("new-year.html", new_year = newYear)

@app.route("/articles")
def articles():
    return render_template("articles.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "Please submit via form"
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/note", methods=["GET", "POST"])
def note():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("note.html", notes=notes)