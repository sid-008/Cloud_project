from flask import Flask, request
import sqlite3 as db

app = Flask(__name__)

conn = db.connect("./orders.db")
c = conn.cursor()

c.execute("""create table if not exists orders
(
id integer primary key,
user_id integer,
product_id integer
)
""")


@app.route("/orders/show_all", methods=["GET"])
def login():
    conn = db.connect("./orders.db", check_same_thread=False)
    c = conn.cursor()

    c.execute("select * from orders")

    conn.commit()
    conn.close()

    return "ok"


@app.route("/orders/add", methods=["POST"])
def reg():
    conn = db.connect("./orders.db", check_same_thread=False)
    c = conn.cursor()
    data = request.json
    user_id = data["user_id"]
    prod_id = data["product_id"]

    c.execute(
        f'insert into orders(user_id, product_id) values("{user_id}", "{prod_id}")'
    )

    conn.commit()
    conn.close()

    return "ok"


if __name__ == "__main__":
    app.run()
