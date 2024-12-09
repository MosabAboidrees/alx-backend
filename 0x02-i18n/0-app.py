#!/usr/bin/env python3
"""A Basic Flask app.
"""

# Import the Flask class and render_template function from the flask module
from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Disable strict slashes in URL routing
app.url_map.strict_slashes = False

# Define a route for the root URL
@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    # Render the '0-index.html' template
    return render_template('0-index.html')


# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
