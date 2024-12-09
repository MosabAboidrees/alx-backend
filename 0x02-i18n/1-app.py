#!/usr/bin/env python3
"""A Basic Flask app.
"""

# Import Babel from flask_babel for internationalization support
from flask_babel import Babel
# Import Flask and render_template from flask
# for web framework and template rendering
from flask import Flask, render_template


class Config:
    """Represents a Flask Babel configuration.
    """
    # Supported languages for the application
    LANGUAGES = ["en", "fr"]
    # Default locale for the application
    BABEL_DEFAULT_LOCALE = "en"
    # Default timezone for the application
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Create a Flask application instance
app = Flask(__name__)
# Load configuration from the Config class
app.config.from_object(Config)
# Disable strict slashes in URL routing
app.url_map.strict_slashes = False
# Initialize Babel with the Flask app
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    # Render the '1-index.html' template for the home page
    return render_template('1-index.html')


if __name__ == '__main__':
    # Run the Flask application on host '0.0.0.0' and port 5000
    app.run(host='0.0.0.0', port=5000)
