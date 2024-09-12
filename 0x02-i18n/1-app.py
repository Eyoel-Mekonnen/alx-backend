#!/usr/bin/env python3
"""Set up basic Babel."""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Language class."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """Render and return html."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
