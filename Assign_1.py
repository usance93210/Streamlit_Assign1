#Following Tutorial - Assignment Yoonah An - INFS 772
import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
import graphviz as graphviz
import pickle #to load a saved model
import base64 #to open .gif files in streamlit app

# add the title, set header, set a markdown of a section, set sub-header, write caption, set a code, and display mathematical expressions formatted as LaTeX  
st.title("First Assignment for Streamlit App")
st.header("INFS 772")
st.markdown("Yoonah An")
st.subheader("12 April 2025")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# returns a Boolean value. Display a button widget, radio button widge, select widget, multiselect, select slider, and slider widget
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick your gender', ['Male', 'Female'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

# display a numeric input widget, text input widget, date input widget, time input widget, text input widget with more than a line text, file uploader, and color picker
st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

# display balloons for celebration, progress bar, and temporary waiting message during execution
st.balloons()
st.progress(10)
with st.spinner('Wait for it...'):
    time.sleep(10)

#  display a success message, error message, warning message, informational message, and exception message
st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

# display a matplotlib.pyplot figure
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

# display a line chart
df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.line_chart(df)

# display a bar chart
df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.bar_chart(df)

# display an area chart
df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.area_chart(df)

# display an altair chart
df= pd.DataFrame(
    np.random.randn(500, 3),
    columns=['x','y','z'])

c = alt.Chart(df).mark_circle().encode(
    x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z'])

st.altair_chart(c, use_container_width=True)

# display graph objects
st.graphviz_chart('''
    digraph{
     Big_shark -> Tuna
     Tuna -> Mackerel
     Mackerel -> Small_fishes
     Small_fishes -> Shrimp 
     }
''')  

### Build a Machine Learning Application ###
@st.cache(suppress_st_warning=True)
def get_fvalue(val):
feature_dict = {"No":1,"Yes":2}
for key,value in feature_dict.items():
if val == key:
return value
def get_value(val,my_dict):
for key,value in my_dict.items():
if val == key:
return value
app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode=='Home':
st.title('LOAN PREDICTION :')
st.image('loan_image.jpg')
st.markdown('Dataset :')
data=pd.read_csv('test.csv')
st.write(data.head())
st.markdown('Applicant Income VS Loan Amount ')
st.bar_chart(data[['ApplicantIncome','LoanAmount']].head(20))

