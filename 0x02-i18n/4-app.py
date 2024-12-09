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
    """Retrieves the locale for a web page."""
    # Check if the 'locale' parameter exists in the request args
    locale = request.args.get('locale')
    # Validate if the locale is supported
    if locale in app.config["LANGUAGES"]:
        print(f"Selected locale from query parameter: {locale}")
        return locale  # Return the valid locale
    # best_match = request.accept_languages.best_match(app.config["LANGUAGES"])
    # print(f"Selected best match locale: {best_match}")
    # Fall back to the best match based on the Accept-Language header
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('4-index.html')  # Render the index template


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
