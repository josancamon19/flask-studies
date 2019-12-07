from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/home', methods = ['GET', 'POST'])
def home():
    return '<h1>Home with methods GET and POST! </h1>'

# Templates are ways to store all the html Front end data apart
# A simple h1 can be passed directly here, but large things is not ideal

@app.route('/home2')
def home2():
    links = ['https://www.google.com', 'https://www.facebook.com']
    return render_template('templates.html', myvar = 'Flask Example', links = links)

if __name__ == '__main__':
    app.run(debug = True)
