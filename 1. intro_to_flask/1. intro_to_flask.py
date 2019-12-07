from flask import Flask

# core of app
app = Flask(__name__)

# simple route
@app.route('/')
def index():
    return "<p>Hello world :)</p>"

# passing a paramater, <place>, is required, if None an error is thrown
@app.route('/home/<place>')
def home(place):
    return '<h1>You are on the home page from ' + place + '</h1>'

# using methods
@app.route('/home2', methods = ['GET', 'POST'])
def home2():
    return '<h1>Hi from home page 2</h1>'

if __name__ == '__main__':
    app.run(debug = True)
