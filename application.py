"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
from FlaskWebProject import app

if __name__ == '__main__':
    # Use Azure Web App settings if available, otherwise use local dev settings
    HOST = environ.get('WEBSITE_HOSTNAME', 'localhost')
    try:
        PORT = int(environ.get('WEBSITE_PORT', '8000'))
    except ValueError:
        PORT = 8000
        
    # Use ssl_context only in local development
    if HOST == 'localhost':
        app.run(HOST, PORT, ssl_context='adhoc')
    else:
        app.run(HOST, PORT)
