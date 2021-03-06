from flask import Flask, render_template, url_for
import os

app = Flask(__name__)


# Home/Index
@app.route('/')
@app.route('/home')
def index():
    author = "Ronnie Joshua"
    return render_template('home.html', author=author)


# About
@app.route('/about')
def about():
    return render_template('about.html')


# To Solve: https://stackoverflow.com/questions/21714653/flask-css-not-updating
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
