#!/usr/bin/env python3
"""Using request Query to select Locale."""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configures Languages."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """Render template and return it."""
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """Retrieve query string and display locale."""
    locale = request.args.get('locale')
    return (locale or
            request.accept_languages.best_match(app.config['LANGUAGES']))


if __name__ == '__main__':
    app.run(debug=True)
