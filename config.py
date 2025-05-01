import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = '2971343e-c5d9-4bce-a664-56e7d292b42e'

    BLOB_ACCOUNT = 'image30'
    BLOB_STORAGE_KEY = '6g1dmgSmM4xJuujBArXCDZnGUe4kmxavKi2qyCc8qJ3RseIHhZRBLg/9xcclMiLY+oustPrFyXE/+AStKi8CwQ=='
    BLOB_CONTAINER = 'image'

    SQL_SERVER = 'cmstan2.database.windows.net'
    SQL_DATABASE = 'cms'
    SQL_USER_NAME = 'sqladmin'
    SQL_PASSWORD = '!pwd1234'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "5038Q~N~2KCnaRV3gov~STzRepw6hcINpKXh4b9z"
    
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    if not CLIENT_SECRET:
        raise ValueError("Need to define CLIENT_SECRET environment variable")

    # AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/ff873fe8-6631-416d-9262-bdbd56117dae"

    CLIENT_ID = "416d6f76-eb16-48ac-a864-59b8326309a1"

    REDIRECT_PATH = "https://cmstan-cbb6f4a4auavfpab.southeastasia-01.azurewebsites.net/"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
