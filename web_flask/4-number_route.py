#!/usr/bin/python3
''' script that starts a Flask web application '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def holis():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def isC(text):
    t = text.replace("_", " ")
    return 'C {}'.format(t)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pitonxd(text='is cool'):
    t = text.replace("_", " ")
    return 'Python {}'.format(t)


@app.route('/number/<n>', strict_slashes=False)
def num(n):
    try:
        if n.isdigit():
            return '{} is number'.format(n)
        elif n.startswith('-') and n[1:].isdigit():
            return '{} is number'.format(n)
    except:
        pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
