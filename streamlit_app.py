import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
#st.write('Hello world! ')

st.header('st.write()')

#%% Day 3
#if st.button('Say hello'):
   #st.write('why hello there')
#else:
   #st.write('goodbye')

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
    x='a', y='b', size='c',color='c', tooltip=['a','b','c']
    )
st.write(c)



