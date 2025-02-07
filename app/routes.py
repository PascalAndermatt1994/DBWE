from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jochen'}
    posts = [
 {
 'author': {'username': 'Paul'},
 'body': 'Schöner Abend hier in Zürich!'
 },
 {
 'author': {'username': 'Susanne'},
 'body': 'Der Unterricht war heute mal gut!'
 }
 ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)