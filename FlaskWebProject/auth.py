from flask import Flask, redirect, url_for, session, request
from flask import render_template
import msal

app = Flask(__name__)
app.secret_key = '3kM8Q~dfKLfiSpRHDvQpJfEAJSGhAbLgr6i_5dsR'  # Change this to a random secret key
app.config['SESSION_TYPE'] = 'filesystem'

# Azure AD configuration
CLIENT_ID = '614fd590-1b5f-4e1f-bfc1-812ed33f9895'  # Application (client) ID
CLIENT_SECRET = 'kRY8Q~UQLwLj4yBomCVIeZgMCgI0peS7K9LA4bx2'  # Client secret
TENANT_ID = 'ff873fe8-6631-416d-9262-bdbd56117dae'  # Directory (tenant) ID
AUTHORITY = f'https://login.microsoftonline.com/ff873fe8-6631-416d-9262-bdbd56117dae'
REDIRECT_URI = 'https://udacitycms-hee2d4eyhgabgqa2.southeastasia-01.azurewebsites.net'  # Redirect URI

# Scopes for the API
SCOPE = ['User.Read']  # Add other scopes as needed

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    # Create a new MSAL app instance
    msal_app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET,
    )
    # Generate the authorization URL
    auth_url = msal_app.get_authorization_request_url(SCOPE, redirect_uri=REDIRECT_URI)
    return redirect(auth_url)

@app.route('/getAToken')
def get_a_token():
    # Create a new MSAL app instance
    msal_app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET,
    )
    # Get the authorization code from the request
    code = request.args.get('code')
    # Exchange the authorization code for a token
    result = msal_app.acquire_token_by_authorization_code(code, scopes=SCOPE, redirect_uri=REDIRECT_URI)
    
    if 'access_token' in result:
        session['access_token'] = result['access_token']
        return redirect(url_for('profile'))
    else:
        return 'Error obtaining token: ' + str(result.get('error'))

@app.route('/profile')
def profile():
    if 'access_token' in session:
        return 'Access Token: ' + session['access_token']
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
