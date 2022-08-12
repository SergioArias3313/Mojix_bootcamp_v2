import streamlit as st
import pandas as pd
from  PIL import Image

st.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier")
st.caption('Simple but effective tips for every python lovers')

# add photo
image = Image.open('image_1.png')
st.image(image, caption='Photo by Miesha Maiden from Pexels')




st.markdown('The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can urprise you with their amazing capabilities.')
st.markdown('In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.')
st.markdown('                                    . . .')

st.header('1. Walrus operator')
st.markdown('The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.')

#---------------------------
st.subheader('Example')
code_1 = ''' Mylist = [1,2,3]
    if(l := len(mylist) > 2):
        print(l) '''

st.code(code_1, language='python')

st.subheader('Output')
code_2 = ''' 3 '''
st.code(code_2, language='python')

#----------------------------

st.header('2. Splitting a string')
st.markdown('If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!')

st.subheader('Example')
code_2_1 = ''' string = "hello world"
string.split()'''
st.code(code_2_1, language='python')

st.subheader('Output')
code_2_2 = ''' ['hello', 'world']'''
st.code(code_2_2, language='python')

#---------------------------
st.header('3. Reversing a string')
st.markdown('If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.')

st.subheader('Example')
code_3_1 = ''' str = "hello world!"
    a=str[::-1]
    print(a)'''
st.code(code_3_1, language='python')

st.subheader('Output')
code_3_2 = '''!dlrow olleh'''
st.code(code_3_2, language='python')

#------------- 4 -------------

st.header('4. Merging two dictionaries')
st.markdown('This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use ** in front of the name of the two dictionaries like below two merge them into a single dictionary:') 
st.subheader('Example')

code_4_1 = ''' d1 = {“a”: 10, “b”:20}
d2 = {“c”: 30, “d”:40}
d3 = {**d1, **d2}
print(d3)'''

st.code(code_4_1, language='python')

st.subheader('Output')
code_4_2 = '''{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}'''
st.code(code_4_2, language='python')

#------------- 5 -----------------

st.header('5. The zip() function')
st.markdown('The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.') 
st.subheader('Example')

code_5_1 = ''' colour = [“red”, “yellow”, “green”]
fruits = [‘apple’, ‘banana’, ‘mango’]
for colour, fruits in zip(colour, fruits):
print(colour, fruits)'''

st.code(code_5_1, language='python')

st.subheader('Output')
code_5_2 = '''red apple
yellow banana
green mango'''

st.code(code_5_2, language='python')
st.markdown('The zip() function can also be used for combining two lists into a dictionary. This method can be really helpful while grouping data from the list.')

st.subheader('Example')
code_5_3 = '''[“Rajesh”, “kumar”, “Kriti”]
marks = [87, 90, 88]
dictionary = dict(zip(students, marks))
print(dictionary)'''

st.code(code_5_3, language='python')

st.subheader('Output')
code_5_4 = '''{‘Rajesh’: 87, ‘kumar’: 90, ‘Kriti’: 88}'''

st.code(code_5_4, language='python')