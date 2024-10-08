#!/usr/bin/env python3
"""Apply Babel Translation."""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Create class for Locale and Time Zone."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """Return rendered index.html."""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """Select Language preference."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
