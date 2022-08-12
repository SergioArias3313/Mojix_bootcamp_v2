import streamlit as st
import pandas as pd

st.write("Let's star with the tricks")

Mylist = [1,2,3]
if(l := len(mylist) > 2): 
    print(l)
    st.write(l)