#!/usr/bin/env python3
"""A Basic Flask app with internationalization support.
"""
# Import Babel from flask_babel for internationalization support
from flask_babel import Babel
# Import Flask, render_template, and request from flask
from flask import Flask, render_template, request


class Config:
    """Represents a Flask Babel configuration.
    """
    # Define the supported languages
    LANGUAGES = ["en", "fr"]
    # Set the default locale to English
    BABEL_DEFAULT_LOCALE = "en"
    # Set the default timezone to UTC
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Create a Flask application instance
app = Flask(__name__)
# Load the configuration from the Config class
app.config.from_object(Config)
# Disable strict slashes in URL routing
app.url_map.strict_slashes = False
# Initialize Babel with the Flask app
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.
    """
    # Determine the best match for supported languages from the request
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    # Render the index template
    return render_template('3-index.html')


if __name__ == '__main__':
    # Run the Flask app on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
