from flask import Flask
import sqlite3

from flask import Flask, render_template, request, url_for,redirect
from flask_bootstrap import Bootstrap
from forms import LoginForm, SignUpForm
from data_processing import *
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin


app = Flask(__name__)
app.secret_key="github1203"
bootstrap = Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self):
        super().__init__(is_authenticated, is_active, is_anonymous, get_id())

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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
    #TODO: setup a nice dashboard


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for())

if __name__ == '__main__':
    app.run(debug=True)

