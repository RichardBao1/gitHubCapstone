from flask import Flask
import sqlite3

from flask import Flask, render_template, request, url_for,redirect
from flask_bootstrap import Bootstrap
from forms import LoginForm, SignUpForm
from data_processing import *


app = Flask(__name__)
app.secret_key="github1203"
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        form_info = request.form
        username, password = form_info['username'], form_info['password']
        if checkPassword(username, password):
            #if login works
            return redirect(url_for('dashboard'))
        else:
            #if login does not work
            return redirect(url_for('login_page'))
    return render_template('login.html', form=form)
    # return render_template('loginPage.html, form=form')

@app.route('/signup', methods = ['GET', 'POST'])
def signup_page():
    form = SignUpForm()
    if form.validate_on_submit():
        form_info = request.form
        username,password,email,phone = form_info['username'], form_info['password'],\
                                        form_info['email'], form_info['phone']
        try:
            addUser(username,password,email,phone)
            return redirect(url_for('signedUp'))
        except:
            return 'nice'
    return render_template('signUp.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/signedUp')
def signedUp():
    return render_template('signedUp.html')

if __name__ == '__main__':
    app.run(debug=True)

