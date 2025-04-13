#Following Tutorial - Assignment Yoonah An - INFS 772
import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt


st.title("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.subheader("Image :")
st.image("My_pic.jpg")

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick your gender', ['Male', 'Female'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')


st.balloons()
st.progress(10)
with st.spinner('Wait for it...'):
    time.sleep(10)

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))


rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.line_chart(df)

df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.bar_chart(df)

df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.area_chart(df)

df= pd.DataFrame(
    np.random.randn(500, 3),
    columns=['x','y','z'])

c = alt.Chart(df).mark_circle().encode(
    x='x' , 'y'=y , size='z', color='z', tooltip=['x', 'y', 'z'])

st.altair_chart(c, use_container_width=True)
