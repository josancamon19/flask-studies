from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter

app = Flask(__name__)
host = 'sql10.freemysqlhosting.net'
db_name = 'sql10289291'
db_username = 'sql10289291'
db_pass = 'BaZTUCBC2K'
uri = 'mysql://'+db_username+':'+db_pass+'@'+host+'/'+db_name

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SECRET_KEY'] = 'secret_key'
# just put as true for Flask user
app.config['CSRF_ENABLED'] = True
app.config['EMAIL_ENABLED'] = False
Bootstrap(app)

db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False, server_default = '')
    active = db.Column(db.Boolean(), nullable = False, server_default = '0')

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)

@app.route('/')
def index():
    return 'This is the home page'

@app.route('profile')
def profile():
    return 'This is the protected page'

if __name__ == '__main__':
    app.run(debug = True)
