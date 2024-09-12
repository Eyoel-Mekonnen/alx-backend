#!/usr/bin/env python3
"""Set up basic Flask app."""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def home():
    """Render template html."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
