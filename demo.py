# main.py
import streamlit as st
from src.components.auth import authenticate_user

# Azure AD configuration
client_id = "95d75130-08e9-4d56-935f-1cc063a81177"
client_secret = "uwS8Q~6_ulnMHVmqzGKHT7QFX5pToKls57CicciS"
authority = "https://login.microsoftonline.com/64dc69e4-d083-49fc-9569-ebece1dd1408"
redirect_uri = "https://streamlit-auth-msal-streamlit.apps.cluster-srkhk.dynamic.redhatworkshops.io"

# Function to check if the user is authenticated
def is_authenticated():
    return "access_token" in st.session_state

# Streamlit app
st.title("Streamlit Azure OIDC Example")

# Check if the user is authenticated
if not is_authenticated():
    # Display login link
    auth_url = f"{authority}/oauth2/v2.0/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&response_mode=query&scope=openid%20profile&state=12345"
    st.markdown(f"[Login with Azure AD]({auth_url})")

    # Get authorization code from user input
    auth_code = st.text_input("Enter Authorization Code:")

    # Check if the authorization code is provided
    if auth_code:
        # Authenticate the user and store the access token in session_state
        access_token = authenticate_user(client_id, client_secret, auth_code, authority, redirect_uri)
        st.session_state.access_token = access_token
        st.success("Authentication successful!")

# If the user is authenticated, display content
if is_authenticated():
    st.write("Access Token:", st.session_state.access_token)
    st.write("Streamlit content goes here...")

