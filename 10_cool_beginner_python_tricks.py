import streamlit as st
import pandas as pd

st.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier")
st.markdown('Simple but effective tips for every python lovers')

st.markdown('The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can urprise you with their amazing capabilities.')
st.markdown('In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.')
st.markdown('                                    . . .')

st.header('1. Walrus operator')
st.markdown('The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.')

st.subheader('Example')
code_1 = ''' Mylist = [1,2,3]
    if(l := len(mylist) > 2):
        print(l) '''

st.code(code_1, language='python')

st.subheader('Output')
code_2 = ''' 3 '''
st.code(code_2, language='python')

st.header('2. Splitting a string')