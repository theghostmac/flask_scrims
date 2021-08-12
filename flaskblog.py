from flask import Flask, render_template, redirect, url_for
from logging import debug
from flask_bootstrap import Bootstrap

#initializing in bootstrap variable
app = Flask(__name__)

bootstrap = Bootstrap(app)

posts = [
    {
        'author': 'Ghost Mac',
        'title': 'Blog Post 1',
        'content': 'Technical writeup',
        'datePosted': 'July 13th, 2021'
    },
    {
        'author': 'Sparkie Drounz',
        'title': 'Blog Post 2',
        'content': 'UIUX Writeup',
        'datePosted': 'June 31st, 2021'
    }
]
#initializing app
#(signature: GhostMac)

@app.route('/')
def index():
    return "Welcome to My Simple Blog."

name = "GhostMac"
#user handle
@app.route('/<name>')
def user(name):
    return render_template('user.html', name=name)

#creating home page
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

#creating redirect option
@app.route('/admin')
def redirect():
    return redirect(url_for('home'))

#creating about page
@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)