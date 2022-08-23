import streamlit as st
import pandas as pd
import numpy as np

"""
# Hello pyladies
## hello gentlemen
Here's our first attempt at using data to create a table:
"""

st.write("Hello, this is my first streamlit app")

#text = Hello
#text ###this is a magic command and works same as st.write(text)

df = pd.DataFrame({
    'column A' : [1,2,3,4],
    'column B' : [10,20,30,40],

})

st.write(df)

#st.table(df) #displays static table

df2 = pd.DataFrame(np.random.randn(10,20),
columns = ('col %d' % i for i in range(20)))

st.dataframe(df2.style.highlight_max(axis=0))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

#x = st.slider('number of lessons')

#st.write('With', x, 'lessons you earn', 20*x, 'EUR')

y = st.sidebar.slider('number of lessons sidebar')

#st.sidebar.write("This is a number of lessons", y)

st.write("This is a number of lessons", y)

st.text_input("Your name", key="name")

st.session_state.name

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.table(chart_data.style.highlight_max(axis=0))












