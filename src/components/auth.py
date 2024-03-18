# auth.py

import requests
from msal import ConfidentialClientApplication

def authenticate_user(client_id, client_secret, auth_code, authority, redirect_uri):
    app = ConfidentialClientApplication(
        client_id,
        authority=authority,
        client_credential=client_secret,
    )
    token_response = app.acquire_token_by_authorization_code(
        auth_code, redirect_uri, scopes=["openid", "profile"]
    )
    return token_response.get("access_token")
