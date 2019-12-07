from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

nav = Nav(app)

view1 = View('Home Page', 'index')
view2 = View('Item One', 'items', item = 1)
link1 = Link('Google', 'https://www.google.com')
sep1 = Separator()
text = Text('Here is some text')
subgroup = Subgroup('Subgroup', view1, view2, link1)
navbar = Navbar('name_doesnt_matter', view1, view2, link1, text, subgroup)
nav.register_element('my_navbar',navbar)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/items/<item>')
def items(item):
    return '<h1>The item is {}</h1>'.format(item)

if __name__ == '__main__':
    app.run(debug = True)
