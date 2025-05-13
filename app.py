from flask import Flask, request, render_template, make_response, redirect
import sqlite3
import os
import jwt

app = Flask(__name__)
SECRET_KEY = "secret"  # Clé volontairement faible

def init_db():
    if not os.path.exists("database.db"):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("CREATE TABLE users (username TEXT, password TEXT)")
        c.execute("INSERT INTO users VALUES ('admin', 'supersecret')")
        c.execute("INSERT INTO users VALUES ('user1', 'password')")
        conn.commit()
        conn.close()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        conn.close()

        if result:
            token = jwt.encode({"user": username}, SECRET_KEY, algorithm="HS256")
            resp = make_response(redirect("/dashboard"))
            resp.set_cookie("token", token)
            return resp

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    token = request.cookies.get("token")
    if not token:
        return redirect("/")

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"],
            options={"verify_signature": False}
        )
        user = payload.get("user", "")
        if user == "admin":
            return "<h1>Bienvenue admin ! FLAG{jwt_authentication_broken}</h1>"
        return f"<h1>Bienvenue {user}</h1>"
    except Exception as e:
        return f"Token invalide: {e}", 403

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=80, debug=True)
