#!/usr/bin/env python3
"""A Basic Flask app with internationalization support.
"""
from flask_babel import Babel
from flask import Flask, render_template, request


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


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.
    """
    # Decode and split query string
    queries = request.query_string.decode('utf-8').split('&')
    # Parse query parameters
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_table:  # Check if 'locale' is in query parameters
        if query_table['locale'] in app.config["LANGUAGES"]:  # Validate locale
            return query_table['locale']  # Return the locale if valid
    # Return the best match locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('4-index.html')  # Render the index template


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
