import streamlit as st
from datetime import date
import pandas as pd
import numpy as np

def creds_entered():
    if st.session_state["user"].strip() == "admin" and st.session_state["passwd"].strip() == "admin":
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["passwd"]:
            st.warning("Please enter password")
        elif not st.session_state["user"]:
            st.warning["Please enter username"]
        else:
            st.error("Invalid Username/Pass :face_with_raised_eyebrow: :man-shrugging: :yawning_face:")

def authenticate_user():
    if "authenticated" not in st.session_state:
        st.text_input(label="Username:", value="", key="user", on_change=creds_entered)
        st.text_input(label="Password:", value="", key="passwd", on_change=creds_entered)
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(label="Username:", value="", key="user", on_change=creds_entered)
            st.text_input(label="Password:", value="", key="passwd", on_change=creds_entered)
            return False

if authenticate_user():

    st.title("Hello streamlit :100: :the_horns:")

    st.header("Header :anchor:")

    st.subheader("Sub Header :taurus:")

    st.text('This is a trial of text')

    st.latex(r'''
        a + ar + a r^2 + a r^3 ''',help='This is latex function to display mathematical functions')

    st.markdown(""" ### h3 tag :moon: :sunglasses: :cool: """)

    df = pd.DataFrame.from_dict({ 'name': ['Yoda', 'John Wick', 'Pikachu'],
           'country': ['Star', 'USA', 'Japan'],
           'dob': [date.today().strftime("%B %d, %Y"), date(2002,5,5), date(1992,12,12)] })

    st.write(df)

    data_csv = pd.read_csv("data//Salary_Data.csv")

    st.dataframe(data_csv,width=1500,height=300)
