import sqlite3
from flask import g
from hashlib import pbkdf2_hmac

salt = b'\xfa#\xb3\xd5\x1ac\xa4\xce2\x8f\xdf*\xfb\xc6\x8f\x99\x18\\{\xce-\xd0\xb4\x93\x97\xf3\xa0\xabbjV/'


DATABASE = 'login.db'

def establishConnection(func):
    #saves code repetition so i don't have to write conn = ... cur = ... everytime
    def connection(*args, **kwargs):
        conn = sqlite3.connect(DATABASE)
        try:
            cur = conn.cursor()
            rv = func(cur, *args, **kwargs)
        except Exception as e:
            conn.rollback()
            raise e
        else:
            if rv == None: #if you don't return anything i.e. not a SELECT keyword
                conn.commit()
        finally:
            conn.close()

        if rv != None:
            return rv
    return connection




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

def getHash(password):
    #return pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    #return str(hash(password))
    return password


@establishConnection
def createTable(cur):
    cur.execute('''CREATE TABLE user
                (id INTEGER not null primary key autoincrement,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE)''')
    #id INTEGER not null primary key autoincrement
    #could just be id INTEGER primary key - as integer primary keys default autoincrement
    #when null value is passed in autoincrement, id value is one larger then
    #previous largest value to exist in that column

@establishConnection
def getData(cur, userId):
    cur.execute("SELECT * FROM user WHERE id=?", (userId,))
    return cur.fetchall()

@establishConnection
def addUser(cur, username, password, email, phone):
    password = getHash(password)
    cur.execute("INSERT INTO user (username, password, email, phone) VALUES (?, ?, ?, ?)",
                (username, password, email, phone))

@establishConnection
def deleteUser(cur, userId):
    cur.execute("DELETE FROM user WHERE id =?", (userId,))


@establishConnection
def updatePassword(cur, userId, newPassword):
    password = getHash(newPassword)
    cur.execute("UPDATE user SET password=? WHERE id=?", (password, userId))

@establishConnection
def getUsername(cur, userId):
    cur.execute("SELECT username FROM user WHERE id=?", (userId,))
    return cur.fetchone()[0]

@establishConnection
def getUserId(cur, username):
    cur.execute("SELECT id FROM user WHERE username=?", (username,))
    val = cur.fetchone()
    return val[0] if val else None

@establishConnection
def checkPassword(cur, username, password):
    password = getHash(password)
    try:
        cur.execute("SELECT password FROM user WHERE username=?", (username,))
        if getHash(cur.fetchone()[0])== password:
            return True
        else:
            return False
    except:
        return False


