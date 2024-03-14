import streamlit as st
from datetime import date
import pandas as pd

# from src.components.auth import authenticate_user


import streamlit as st
import requests
from msal import ConfidentialClientApplication

# Azure AD configuration
client_id = "95d75130-08e9-4d56-935f-1cc063a81177"
client_secret = "uwS8Q~6_ulnMHVmqzGKHT7QFX5pToKls57CicciS"
authority = "https://login.microsoftonline.com/64dc69e4-d083-49fc-9569-ebece1dd1408"
redirect_uri = "https://streamlit-msal-xom.apps.cluster-ckl5q.dynamic.redhatworkshops.io"

# Function to authenticate the user and retrieve access token
def authenticate_user(auth_code):
    app = ConfidentialClientApplication(
        client_id,
        authority=authority,
        client_credential=client_secret,
    )
    token_response = app.acquire_token_by_authorization_code(
        auth_code, redirect_uri, scopes=["openid", "profile"]
    )
    return token_response.get("access_token")

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
        st.session_state.access_token = authenticate_user(auth_code)
        st.success("Authentication successful!")

# If the user is authenticated, display content
if is_authenticated():
    st.write("Access Token:", st.session_state.access_token)
    st.write("Streamlit content goes here...")



# def streamlit_app():
#     if authenticate_user():
#         st.title("Hello :red[streamlit] :100: :the_horns:")

#         st.header("Header :anchor:")

#         st.subheader("Sub Header :taurus:")

#         st.text("This is a trial of text")

#         st.latex(
#             r"""
#             a + ar + a r^2 + a r^3 """,
#             help="This is latex function to display mathematical functions",
#         )

#         st.markdown(""" ### h3 tag :moon: :sunglasses: :cool: """)

#         df = pd.DataFrame.from_dict(
#             {
#                 "name": ["Yoda", "John Wick", "Pikachu"],
#                 "country": ["Star", "USA", "Japan"],
#                 "dob": [
#                     date.today().strftime("%B %d, %Y"),
#                     date(2002, 5, 5),
#                     date(1992, 12, 12),
#                 ],
#             }
#         )

#         st.write(df)

#         data_csv = pd.read_csv("data//Salary_Data.csv")

#         st.dataframe(data_csv, width=1500, height=300)


# if __name__ == "__main__":
#     streamlit_app()
