from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dave'}
    posts = [
        {
            'author': {'username': 'Connor'},
            'body': 'Trier is hot today!'
        },
        {
            'author': {'username': 'Karen'},
            'body': 'Make sure you take a hat and water with you!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)