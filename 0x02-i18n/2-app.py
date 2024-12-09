#!/usr/bin/env python3
"""A Basic Flask app.
"""
# Import Babel from flask_babel for internationalization support
from flask_babel import Babel
# Import Flask, render_template, and request from flask
from flask import Flask, render_template, request


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]  # Define the supported languages
    BABEL_DEFAULT_LOCALE = "en"  # Set the default locale to English
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Set the default timezone to UTC


app = Flask(__name__)  # Create a Flask application instance
app.config.from_object(Config)  # Load configuration from the Config class
app.url_map.strict_slashes = False  # Disable strict slashes in URL routing
babel = Babel(app)  # Initialize Babel with the Flask app


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.
    """
    # Determine the best match for supported languages
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('2-index.html')  # Render the index page template


if __name__ == '__main__':
    # Run the Flask app on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
