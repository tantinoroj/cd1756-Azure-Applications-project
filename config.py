import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'ac2df92a-66cf-4f47-875b-f5d027c33934'

    BLOB_ACCOUNT = 'images99'
    BLOB_STORAGE_KEY = 'IXy2NpG/ghgh6dRlhR5JBBi8IlK8MDxIJkBGdQBc8XlZs5Jp3DGD6PVQQS1/0JHXdtWT/KQuf+aO+AStesXKRA=='
    BLOB_CONTAINER = 'images'

    SQL_SERVER = 'cms-server'
    SQL_DATABASE = 'cms'
    SQL_USER_NAME = 'cmsadmin'
    SQL_PASSWORD = 'CMS4dmin'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "kRY8Q~UQLwLj4yBomCVIeZgMCgI0peS7K9LA4bx2"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    if not CLIENT_SECRET:
        raise ValueError("Need to define CLIENT_SECRET environment variable")

    # AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/ff873fe8-6631-416d-9262-bdbd56117dae"

    CLIENT_ID = "614fd590-1b5f-4e1f-bfc1-812ed33f9895"

    REDIRECT_PATH = "https://udacitycms-hee2d4eyhgabgqa2.southeastasia-01.azurewebsites.net/"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
