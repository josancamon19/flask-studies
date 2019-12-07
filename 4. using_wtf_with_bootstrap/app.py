from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sec_key'
app.config['TESTING'] = True

Bootstrap(app)

class LoginForm(FlaskForm):
    username = StringField('username', validators = [InputRequired(), Email('Pass a real email')])
    password = StringField('password', validators = [InputRequired(), Length(min = 7, )])

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Form Succesfully submited'
    return render_template('index.html', form = form)

if __name__ == '__main__':
    app.run(debug = True)
