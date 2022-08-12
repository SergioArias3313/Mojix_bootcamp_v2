import streamlit as st
import pandas as pd

st.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier")
st.markdown('The compactness of Python can make a developer’s life a lot easier when writing')
st.markdown('lines and lines of code. But there are some lesser-known Python tricks that can')
st.markdown('surprise you with their amazing capabilities.')

st.subheader('example')
st.code("Mylist = [1,2,3]")
st.code("if(l := len(mylist) > 2)")
st.code( " print(l)")

st.subheader('Output')
st.write("3")
