#!/usr/bin/env python3

"""A Basic Flask app with internationalization support.
"""

from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]  # Supported languages
    BABEL_DEFAULT_LOCALE = "en"  # Default locale
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


app = Flask(__name__)  # Create a Flask application instance
app.config.from_object(Config)  # Load configuration from Config class
app.url_map.strict_slashes = False  # Disable strict slashes
babel = Babel(app)  # Initialize Babel with the Flask app

# Dictionary of users with their respective locale and timezone
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on a user id.
    """
    # Get login_as parameter from request
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))  # Return user if found
    return None  # Return None if no user found


@app.before_request
def before_request() -> None:
    """Performs some routines before each request's resolution.
    """
    user = get_user()  # Retrieve user based on login_as parameter
    g.user = user  # Store user in Flask's global object


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.
    """
    # Get locale parameter from request
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale  # Return locale if supported
    # Return best match locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    # Render the index page template
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
