import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

st.header("Day 5")

st.header("st.headr")
st.markdown(""" This is a streamlit app, markdown   """)

st.write('Hello, *World!* :sunglasses: ,write' )
st.write('Hello, *World!* :sunglasses: ,write' )

st.write('Hello, *World!* :sunglasses: ,write' )


df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
st.write("Below is a df", df, "above is a df")
st.header("st.headr")
st.subheader('This is a subheader')
st.caption('This is a string that explains something above.')
st.markdown('Streamlit is **_really_ cool**.')
