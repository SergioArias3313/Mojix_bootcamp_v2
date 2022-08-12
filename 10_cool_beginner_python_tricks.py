import streamlit as st
import pandas as pd

st.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier")
st.markdown('The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can urprise you with their amazing capabilities.')

st.subheader('Example')
code_1 = ''' Mylist = [1,2,3]
    if(l := len(mylist) > 2):
        print(l) '''

st.code(code_1, language='python')

st.subheader('Output')
st.write("3")
