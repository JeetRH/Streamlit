import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
