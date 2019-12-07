from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length
app = Flask(__name__)

app.config['SECRET_KEY'] = 'this_is_my'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeeAaAUAAAAAEUBQJIniSTot1JbvlxO_AsdE3wD'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LeeAaAUAAAAAAEEt84MlG4ZTZWwI_vXMlEVFcnN'
# recaptcha is throwing an error cause the addresses paassed
# (in recapchta registration for be able to use it) I just included localhost
app.config['TESTING'] = True

class LoginForm(FlaskForm):
    username = StringField('username', validators = [InputRequired(message ='Completalo'), Length(min = 5, max = 10, message = 'Must be between 5 and 10')])
    password = PasswordField('password', validators = [InputRequired()])
    recaptcha = RecaptchaField()


@app.route('/form', methods = ['GET', 'POST'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        return 'The username is {}, the password is {}'.format(form.username.data, form.password.data)
    return render_template('form.html', form = form)


if __name__ == '__main__':
    app.run(debug=True)
