#!/usr/local/bin/python3
from flask import Flask
from flask.logging import create_logger
import logging

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

app = Flask(__name__)

@app.route("/")
@app.route('/home')
def home():
    user = {'username': 'Ayoyinka'}
    posts = [
        {
            'author': {'username': 'UdacityTutor'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'UdacityStudent'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return """<html>
    <head>
        {% if title %}
        <title>{{ title }} - Microblog</title>
        {% else %}
        <title>Welcome to Microblog</title>
        {% endif %}
    </head>
    <body>
        <h1>Hi, {{ user.username }}!</h1>
        {% for post in posts %}
        <div><p>{{ post.author.username }} says: <b>{{ post.body }}</b></p></div>
        {% endfor %}
    </body>
</html>"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
