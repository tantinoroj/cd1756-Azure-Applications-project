import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = '26dd918b-e70d-4470-b328-137159187428'

    BLOB_ACCOUNT = 'cmstan'
    BLOB_STORAGE_KEY = 'l3dXxrnSbhUWkB4qBZy5bPjzRGeqnK0KXuJbMVTd1OP5+VfMnAZg51MKJsYDpveeMIzb4lVY/+x/+AStUpeGKA=='
    BLOB_CONTAINER = 'images'

    SQL_SERVER = 'cmstan'
    SQL_DATABASE = 'cms'
    SQL_USER_NAME = 'sqladmin'
    SQL_PASSWORD = '!pwd1234'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "kAZ8Q~h21nWxTOyd85KKfkgRsDSeGYGLnLZF7ap3"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    if not CLIENT_SECRET:
        raise ValueError("Need to define CLIENT_SECRET environment variable")

    # AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/f958e84a-92b8-439f-a62d-4f45996b6d07"

    CLIENT_ID = "cd8e5735-7129-4065-9538-2a3499e29835"

    REDIRECT_PATH = "https://cmstan-cbb6f4a4auavfpab.southeastasia-01.azurewebsites.net/"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
