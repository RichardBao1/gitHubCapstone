from flask import Flask
import sqlite3
import data_processing

from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key="hlkjhkljhl"
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return 'Hello World!'



if __name__ == '__main__':
    app.run()

