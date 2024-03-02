import streamlit as st
from datetime import date
import pandas as pd

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
