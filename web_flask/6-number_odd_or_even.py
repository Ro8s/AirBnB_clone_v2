#!/usr/bin/python3
''' script that starts a Flask web application '''
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    if type(n) is int:
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if type(n) is int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    kind=""
    if (n % 2 == 0):
        kind = "even"
    else:
        kind = "odd"
    return render_template('6-number_odd_or_even.html', n=n, kind=kind)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
