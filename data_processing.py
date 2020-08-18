import sqlite3
from flask import g

DATABASE = 'login.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def createTable():
    conn = sqlite3.connect('login.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE user
                (id INTEGER not null primary key autoincrement,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE)''')
    conn.commit()
    conn.close()

def addUser(username, password, email, phone):
    query_db("INSERT INTO user (username, password, email, phone) VALUES (?, ?, ?, ?)",
             (username, password, email, phone))

def checkPassword(username, password):
    conn = sqlite3.connect('login.db')
    cur = conn.cursor()

    conn.commit()
    conn.close()


addUser('johnJones', 'password2', 'iio@gmail.com', 'oipu')