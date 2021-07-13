from logging import debug
from flask import Flask, render_template

#naming app
app = Flask(__name__)

# posts = [
#     {
#         'author': 'Ghost Mac',
#         'title': 'Blog Post 1',
#         'content': 'Technical writeup',
#         'datePosted': 'July 13th, 2021'
#     },
#     {
#         'author': 'Sparkie Drounz',
#         'title': 'Blog Post 2',
#         'content': 'UIUX Writeup',
#         'datePosted': 'June 31st, 2021'
#     }
# ]
#initializing app
#(signature: GhostMac)
@app.route('/')
def index():
    return "hello world"
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)
#creating about page
@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)