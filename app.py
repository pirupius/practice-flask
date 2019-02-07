from flask import Flask, render_template

app = Flask(__name__)
app.config['TESTING'] = True
app.config['FLASK_DEBUG'] = True
app.config['FLASK_ENV'] = development
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

if __name__ == '__main__':
    app.run()
