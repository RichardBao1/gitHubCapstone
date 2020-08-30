from flask import Flask
import sqlite3

from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from forms import LoginForm, SignUpForm
from data_processing import *


app = Flask(__name__)
app.secret_key="github1203"
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    a = checkPassword('johnSmith', 'password12')
    print(a)
    return 'Hello World!'

@app.route('/putPage', methods = ['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        form_info = request.form
        return 'go to page after submitting form'
    return 'put some template page'
    # return render_template('loginPage.html, form=form')

@app.route('/putPage', methods = ['GET', 'POST'])
def signup_page():
    form = SignUpForm()
    if form.validate_on_submit():
        form_info = request.form
        username,password,email,phone = form_info['username'], form_info['password'],\
                                        form_info['email'], form_info['phone']
        return 'go to page after submitting form'
    return render_template('signUpPage.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)

