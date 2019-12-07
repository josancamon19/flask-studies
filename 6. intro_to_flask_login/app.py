from flask import Flask, render_template, request, redirect, url_for, flash

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from flask_login import LoginManager, UserMixin
from flask_login import login_user, login_required, logout_user, current_user
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)

# db uri construction
host = 'sql10.freemysqlhosting.net'
db_name = 'sql10289291'
db_username = 'sql10289291'
db_pass = 'BaZTUCBC2K'
uri = 'mysql://'+db_username+':'+db_pass+'@'+host+'/'+db_name

# app configurations
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key'
app.config['TESTING'] = True
Bootstrap(app)

# db creation and login_manager initiated
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# usually only import db.Model but usermixin is useful for dealing with users
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(30), unique = True)
    password = db.Column(db.String(30))

# This piece of code is required
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# form for user registration
class AppForm(FlaskForm):
    inp_req = InputRequired(message = 'The field is required')
    valid_email = Email(message ='Your email is invalid')
    valid_length = Length(min = 8, message = 'Length must be greater than 7')

    email = StringField('email', validators = [inp_req, valid_email])
    password = PasswordField('password', validators = [inp_req, valid_length])

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
    form = AppForm()
    if form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
        try:
            user = User(email = email, password = password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('sign_in'))
        except IntegrityError:
            flash('The email you typed is already registered', 'error')
    return render_template('sign_up.html', form = form)

@app.route('/sign_in', methods = ['GET', 'POST'])
def sign_in():
    form = AppForm()
    if form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email = email).first()
        login_user(user)
        return redirect(url_for('home'))
    return render_template('sign_in.html', form = form)

@app.route('/home')
@login_required
def home():
    return 'The current user is {} and the password is {}'.format(current_user.email, current_user.password)

@app.route('/logout')
def logout():
    logout_user()
    return 'you are now logged out'

if __name__ == '__main__':
    app.run(debug = True)
