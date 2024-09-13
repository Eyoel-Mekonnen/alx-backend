#!/usr/bin/env python3
"""Mocking Logging in."""
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config locale and time zone."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """Return Render template."""
    if g.user:
        username = g.user['name']
    else:
        username = None
    return render_template('6-index.html', name=username)


@babel.localeselector
def get_locale():
    """Determine the Language of user."""
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """Execute before any other method during request."""
    g.user = get_user()


def get_user():
    """Mock Log in."""
    if request.args.get('login_as', type=int):
        user_id = request.args.get('login_as', type=int)
        if user_id in users:
            user_dictionary = users[user_id]
            return user_dictionary
    else:
        return None


if __name__ == '__main__':
    app.run(debug=True)
