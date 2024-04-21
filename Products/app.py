from flask import Flask, request, jsonify
import sqlite3 as db

app = Flask(__name__)


conn = db.connect("./products.db")

c = conn.cursor()

c.execute("""create table if not exists products 
(
id integer primary key,
name text not null,
description text not null,
price integer
)
""")


@app.route("/product/show_all", methods=["GET"])
def login():
    conn = db.connect("./products.db", check_same_thread=False)
    c = conn.cursor()

    c.execute("select * from products")
    rows = c.fetchall()

    conn.commit()
    conn.close()

    return jsonify(rows)


@app.route("/product/add", methods=["POST"])
def reg():
    conn = db.connect("./products.db", check_same_thread=False)
    c = conn.cursor()
    data = request.json
    name = data["name"]
    desc = data["desc"]
    price = data["price"]

    c.execute(
        f'insert into products(name, description, price) values("{name}", "{desc}", "{price}")'
    )

    conn.commit()
    conn.close()

    return "ok"


if __name__ == "__main__":
    app.run()
