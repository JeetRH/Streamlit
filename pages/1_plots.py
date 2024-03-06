import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

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
        st.text_input(label="Password:", value="", key="passwd", type="password", on_change=creds_entered)
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(label="Username:", value="", key="user", on_change=creds_entered)
            st.text_input(label="Password:", value="", key="passwd", type="password", on_change=creds_entered)
            return False

if authenticate_user(): 
    # This generates random data with 100 rows and 3 columns! Pretty cool
    data_np = pd.DataFrame(
        np.random.randn(100,3),
        columns=['hot','cold','warm']
    )
    
    #st.write(data_np)
    
    #st.line_chart(data_np)
    
    #st.area_chart(data_np)
    
    #st.bar_chart(data_np)
    
    plt.scatter(data_np['cold'],data_np['warm'])
    plt.title("scatter")
    st.pyplot()
    
    chart = alt.Chart(data_np).mark_circle().encode(
        x = 'cold', y='hot'
    )
    st.altair_chart(chart)
    