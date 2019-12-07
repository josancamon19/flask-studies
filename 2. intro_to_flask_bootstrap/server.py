from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods = ['POST'])
def query():
    query = request.form['q']
    # execute amazon asin read codes 
    return 'query'

if __name__ == '__main__':
    app.run(debug = True)
