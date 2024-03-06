import streamlit as st
from datetime import date
import pandas as pd
import numpy as np


def creds_entered():
    if (
        st.session_state["user"].strip() == "admin"
        and st.session_state["passwd"].strip() == "admin"
    ):
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["passwd"]:
            st.warning("Please enter password")
        elif not st.session_state["user"]:
            st.warning["Please enter username"]
        else:
            st.error(
                "Invalid Username/Pass :face_with_raised_eyebrow: :man-shrugging: :yawning_face:"
            )


def authenticate_user():
    if "authenticated" not in st.session_state:
        st.text_input(label="Username:", value="", key="user", on_change=creds_entered)
        st.text_input(
            label="Password:",
            value="",
            key="passwd",
            type="password",
            on_change=creds_entered,
        )
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(
                label="Username:", value="", key="user", on_change=creds_entered
            )
            st.text_input(
                label="Password:",
                value="",
                key="passwd",
                type="password",
                on_change=creds_entered,
            )
            return False


if authenticate_user():
    a = [4, 5, 6, 98, 45, 36, 22, 78]

    n = np.array(a)

    nd = n.reshape((2, 4))

    data_csv = pd.read_csv("..//data//Salary_Data.csv")

    st.dataframe(data_csv, width=1500, height=300)
    # same output can be achieved through st.write

# We also have st.table to print out the whole table and st.json to print json output like dictionaries
