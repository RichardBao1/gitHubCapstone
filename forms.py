from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField,IntegerField
from wtforms.validators import DataRequired, InputRequired, Length, Email


class SignUpForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=5, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4,max=80)])
    email = StringField('email', validators=[InputRequired(), Email(message = 'Invalid Email'), Length(max=50)])
    phone = IntegerField('Phone Number', validators=[InputRequired()])
    submit = SubmitField('OK')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=5, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4,max=80)])
    remember = BooleanField('remember me')
    submit = SubmitField('OK')

class AuthGitUserForm(FlaskForm):
    username = StringField('username', validators = [InputRequired()])
    submit = SubmitField('OK')

