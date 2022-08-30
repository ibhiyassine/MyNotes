from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required

# Configure application
app = Flask(__name__)



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        email = request.form.get("email")
        password= request.form.get("password")
        rows = db.execute("SELECT * FROM users WHERE email = ?", email)
        if len(rows) == 0 or not check_password_hash(rows[0]["hashword"], password):
            return render_template("login.html", crct_msg=0)
        else:
             session["user_id"] = rows[0]["id"]
             return redirect("/")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])
    the_note = []
    the_note = db.execute("SELECT * FROM notes WHERE user_id = ? AND state = 0", session["user_id"],)
    if request.method == "POST":
        title = request.form.get("title")
        note = request.form.get("note")
        if not title or not note:

            return render_template("index.html", username=username[0]["username"], crct_note=0, the_note=the_note)
        else:
            db.execute("INSERT INTO notes (user_id, title, note) VALUES(?,?,?)", session["user_id"], title, note)
            return redirect("/")
    else:
        search = request.args.get("search")
        if search:
            the_note = db.execute("SELECT * FROM notes WHERE user_id = ? AND state = 0 AND title LIKE ?", session["user_id"], search)
        return render_template("index.html", username = username[0]["username"], the_note=the_note)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method =="POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password= request.form.get("password")
        confirmation = request.form.get("confirm_password")
        if len(username) == 0:
            return render_template("register.html", crct_msg=0)
        elif password == None or len(password) < 8:
            return render_template("register.html", crct_msg=-1)
        elif email == None or email.count("@") != 1:
            return render_template("register.html", crct_msg=-3)
        elif confirmation != password:
            return render_template("register.html", crct_msg=-2)
        else:
            last_check = db.execute("SELECT * FROM users WHERE email = ?", email)
            if len(last_check) > 0:
                return render_template("register.html", crct_msg=-3)
            db.execute("INSERT INTO users (username, hashword, email) VALUES(?, ?, ?)", username, generate_password_hash(password, method='pbkdf2:sha1', salt_length=8), email)
            return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/starred", methods = ["GET", "POST"])
@login_required
def starred():
        username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])
        the_stars = []
        if request.method=="POST":
            title = request.form.get("title")
            note = request.form.get("note")
            star = db.execute("SELECT state FROM notes WHERE user_id = ? AND title = ? AND note = ? LIMIT 1", session["user_id"], title, note)
            if int(star[0]["state"]) == 0:
                db.execute("UPDATE notes SET state = 1 WHERE user_id = ? AND title = ? AND note = ?", session["user_id"], title, note)
            else:
                db.execute("UPDATE notes SET state = 0 WHERE user_id = ? AND title = ? AND note = ?", session["user_id"], title, note)
            return redirect("/starred")
        else:
            search = request.args.get("search")
            if search:
                the_stars = db.execute("SELECT * FROM notes WHERE user_id = ? AND state = 1 AND title LIKE ?", session["user_id"], search)
            else:
                the_stars = db.execute("SELECT * FROM notes WHERE user_id = ? AND state = 1", session["user_id"])
            return render_template("starred.html", the_stars=the_stars, username=username[0]["username"], starred = "starred")

@app.route("/bin")
@login_required
def trashed():
    title = request.args.get("title")
    note = request.args.get("note")
    state = db.execute("SELECT state FROM notes WHERE title = ? AND note = ? LIMIT 1", title, note)
    db.execute("DELETE FROM notes WHERE user_id=? AND title=? AND note=?", session["user_id"], title, note)
    if state[0]["state"] == 0:
        return redirect("/")
    else:
        return redirect("/starred")

@app.route("/settings")
@login_required
def settings():
    username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])
    return render_template("settings.html", username=username[0]["username"])
