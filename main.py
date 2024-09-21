import streamlit as st
from data import get_data
import plotly.express as px

st.title("Data Visualization App")

x_option = st.selectbox(label="Select x-axis data: ",
                      options=("Happiness","GDP",
                               "Generosity","Corruption"))

y_option = st.selectbox(label="Select y-axis data: ",
                      options=("Happiness","GDP",
                               "Generosity","Corruption"))

st.subheader(f"Scatter plot: {x_option} vs {y_option}")

x_data, y_data = get_data(x_option, y_option)
figure = px.scatter(x=x_data, y=y_data, labels={"x": f"{x_option}", "y": f"{y_option}"})
st.plotly_chart(figure)
