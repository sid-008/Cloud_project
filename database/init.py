# This script is to be run only if the
# db does not exist

import sqlite3 as db

conn = db.connect("./cc.db")

c = conn.cursor()

c.execute("""create table if not exists users
(
id integer primary key,
name text not null,
email text not null unique,
address text,
hash text
)""")

c.execute("""create table if not exists products 
(
id integer primary key,
name text not null,
description text not null,
price integer
)
""")

c.execute("""create table if not exists orders
(
id integer primary key,
user_id integer,
product_id integer,
)
""")

# c.execute("""create table stocks
# (date text, trans text, symbol text,
#  qty real, price real)""")


conn.commit()

c.close()
