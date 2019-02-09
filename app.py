from flask import Flask, render_template, flash, redirect, url_for, session, logging, request  
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from data import Articles
from forms import RegisterForm

import pymysql

app = Flask(__name__)
app.config['TESTING'] = True
app.config['FLASK_DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['TEMPLATES_AUTO_RELOAD'] = True

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>')
def article(id):
    return render_template('article.html', id = id)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html')
    return render_template('register.html', form = form)


if __name__ == '__main__':
    app.run()


# fuser 5000/tcp -k