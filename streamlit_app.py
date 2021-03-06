import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
st.set_page_config(layout="wide")

#st.write('Hello world! ')

st.header('st.write()')

#%% Day 3
if st.button('Whos'):
   st.write('Kenza')
else:
   st.write('None')
   
   
###%% 
#Day19

st.header('How to layout your stramlit app')

with st.expander('About this App'):
   st.write("This app shows the various ways on how you can layout your Streamlit App")
   st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=150)
   
st.sidebar.header("Inputs")
user_name = st.sidebar.text_input("What is your name?")
user_emoji = st.sidebar.selectbox("Choose your favorite emoji",['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox("What is your favorite food ?", ['', '🍜','🥜','🥐','🍛','🍔','🍕'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
     st.write(f"Hello {user_name}!")
  else :
     st.write("👈 Please enter your **name**")

with col2:
   if user_emoji != '':
      st.write(f'Your favorite emoji is {user_emjo}')
   else : 
      st.write('👈 Please select an **emoji**')
      
with col3:
   if user_food != '':
      st.write(f"🍴 **{user_food}** is your favorite food")
   else : 
      st.write("👈 Please choose your favorite **food**")
  
   




#%% Day 5

#Example 1
st.write('Hello, *World!* :wave:')
#year=2022
#st.write(f'{year}')

#Example 2
st.write(2022)
 
#Example 3
st.latex(r'''1^{st} DataFrame''')
df=pd.DataFrame({
    'First Column' : [1,2,3,4],
     'Second Column' : [5,6,7,8]
    })
st.write(df)

#Example 4
st.latex(r'''2^{nd} DataFrame''')
df2=pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
    )
c=alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c',color='c', tooltip=['a','b','c'],
    )
st.write(c)

#%%Day8
from datetime import time, datetime

st.header('st.slider')

#Exple 1
st.subheader('slider')
age=st.slider('How old are you ?', 0,130,24)
st.write("I'm",age,'years old')

#Exple2
st.subheader('Range slider')
values=st.slider('select a range of values',0.0,100.0,(25.0, 75.0))
st.write('values:',values)

#Exple3
st.subheader('Range time slider')
appointment=st.slider("Schedule your appointment:", value=(time(9,30),time(12,30)))
st.write("You're scheduled for:",appointment)

#Exple4
st.subheader('Datetime slider')
start_time=st.slider("Select your Datetime:", value=datetime(2022,4,9,10,30), 
                     format="DD/MM/YY - hh:mm")
st.write("Start time:", start_time)                       

#%%Day9
st.header('Line chart')
chart_data=pd.DataFrame(
   np.random.randn(20,3),
   columns=['a','b','c'])
st.line_chart(chart_data)

#%%Day 10
st.header('st.selectbox')

option = st.selectbox(
   "What's your degree ?",
   ('Engineer', 'PhD Student', 'Technician'))
st.write("You're degree is:", option)

#Day11
st.header('st.Multiselect')
options=st.multiselect(
   "What are your favourite colors?",
   ['Green','White','Blue','Gray','Yellow','Pink'],
   ['Green','Blue'])
st.write("Your answer is: ",options)

#Day12
st.header('st.checkbox')

st.write("What would you like to order?")
juice = st.checkbox('Juice')
tea = st.checkbox('Tea')
waffle = st.checkbox('Waffle')

if juice:
   st.write("Here you go 🥤 ")
if tea:
   st.write("Here's your tea 🍵")
if waffle:
   st.write("Miam! looks delicious 🧇")





   

