from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# config is usually done in another file
host = 'sql10.freemysqlhosting.net'
db_name = 'sql10289291'
db_username = 'sql10289291'
db_pass = 'BaZTUCBC2K'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+db_username+':'+db_pass+'@'+host+'/'+db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# the class also preferably created it outside
class Comment(db.Model):
    # table name so should be plural, "Comments"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))
# using console create tables
# python3
# from guestbook.py import db
# db.create_all()
# if there is an error try creating directly from phpmyadmin

@app.route('/')
def index():
    result = Comment.query.all()
    return render_template('index.html', result = result)

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/process', methods = ['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    signature = Comment(name = name, comment = comment)
    db.session.add(signature)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
