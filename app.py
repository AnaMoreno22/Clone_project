
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, usd

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.jinja_env.filters["usd"] = usd

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///travel_planning.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    """Show the trips planned"""
    user_id = session["user_id"]

    trips = db.execute("SELECT * FROM trips WHERE user_id= ?", user_id)
    return render_template("index.html", trips = trips)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    session.clear()

    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username", 400)

        elif not request.form.get("password"):
            return apology("must provide password", 400)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    session.clear()

    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        username_exists = db.execute("SELECT username FROM users WHERE username=?", username)
        if not username:
            return apology("must provide username", 400)

        elif not password or not confirmation:
            return apology("must provide password", 400)

        elif username_exists:
            return apology("username is already taken", 400)

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("must provide equal passwords", 400)

        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password, method='pbkdf2:sha256', salt_length=8))

        return redirect("/login")

    else:
        return render_template("register.html")

@app.route("/add_trip", methods=["POST"])
def add_trip():
    user_id = session["user_id"]
    title = request.form.get("title")
    date = request.form.get("date")
    trip_exists = db.execute("SELECT * FROM trips WHERE title=? AND date=? AND user_id=?", title, date, user_id)
    if not trip_exists:
        if not title:
            return apology("must provide title", 400)
        if not date:
            return apology("must provide date", 400)
        db.execute("INSERT INTO trips (title, date, user_id) VALUES(?, ?, ?)", title, date, user_id)
        return redirect("/")

@app.route("/trip/<id>")
@login_required
def trip(id):
    user_id = session["user_id"]
    plans = db.execute("SELECT plans.date, hotel, restaurant, note, tourist_place, trip_id, plans.id from plans JOIN trips ON trips.id = plans.trip_id WHERE trip_id=? AND trips.user_id = ?", id, user_id)
    trip = db.execute("SELECT title, id from trips WHERE id=? AND user_id = ?", id, user_id)
    return render_template("trip.html", plans = plans, trip = trip)

@app.route("/add_item", methods=["POST"])
def add_item():
    item_date = request.form.get("item_date")
    trip_id = request.form.get("trip_id")
    tourist_place = request.form.get("tourist_place")
    restaurant = request.form.get("restaurant")
    hotel = request.form.get("hotel")
    notes = request.form.get("notes")
    if not item_date:
        return apology("must provide date", 400)
    db.execute("INSERT INTO plans (date, tourist_place, restaurant, hotel, note, trip_id) VALUES(?, ?, ?, ?, ?, ?)", item_date, tourist_place, restaurant, hotel, notes, trip_id)
    url = '/trip/'+str(trip_id)
    return redirect(url)






