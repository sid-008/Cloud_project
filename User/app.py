from flask import Flask, request
import sqlite3 as db

app = Flask(__name__)

conn = db.connect("./users.db")
c = conn.cursor()

c.execute("""create table if not exists users
(
id integer primary key,
name text not null,
email text not null unique,
address text,
hash text
)""")


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/login", methods=["POST"])
def login():
    conn = db.connect("./users.db", check_same_thread=False)
    c = conn.cursor()
    data = request.json
    email = data["email"]
    hash = data["hash"]
    c.execute(
        f'SELECT EXISTS(SELECT 1 FROM users WHERE email="{email}" AND hash = "{hash}")'
    )
    conn.commit()
    conn.close()

    return "logged in"


@app.route("/register", methods=["POST"])
def reg():
    conn = db.connect("./users.db", check_same_thread=False)
    c = conn.cursor()
    data = request.json
    name = data["name"]
    email = data["email"]
    addr = data["address"]
    hash = data["hash"]

    c.execute(
        f'insert into users(name, email, address, hash) values("{name}", "{email}", "{addr}", "{hash}")'
    )
    conn.commit()
    conn.close()

    return "ok"

    # c.execute("""
    # insert into users(name, email, address, hash)
    # values()
    # """)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
