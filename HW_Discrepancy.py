
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#@st.cache(persist = True)

st.title('Inventory discrepancy - Boot camp Mojix2.0')
#file = st.file_uploader('poner el dato', type="csv")

#df = pd.read_csv("C:/Users/sergio/Mojix_bootcamp_v2/output.csv")

df = pd.read_csv("output.csv")
#if df:


st.dataframe(df)
st.markdown("---")

df_1 = df.groupby("Retail_Product_Level1Name").sum()
st.dataframe(df_1)
fig1 = plt.figure(figsize=(10,4))
sns.countplot(x='Unders', data=df_1)
st.pyplot(fig1)

df_2 = df.groupby("Retail_Product_Level2Name").sum()
st.dataframe(df_2)
fig2 = plt.figure(figsize=(10,4))
sns.countplot(x='Unders', data=df_2)
st.pyplot(fig2)

df_3 = df.groupby("Retail_Product_Level3Name").sum()
st.dataframe(df_3)
fig3 = plt.figure(figsize=(10,4))
sns.countplot(x='Unders', data=df_3)
st.pyplot(fig3)


df_4 = df.groupby("Retail_Product_Level3Name").sum()
st.dataframe(df_4)
fig4 = plt.figure(figsize=(10,4))
sns.countplot(x='Unders', data=df_4)
st.pyplot(fig4)


df_5 = df.groupby("Retail_Product_Level3Name").sum()
st.dataframe(df_5)
fig5 = plt.figure(figsize=(10,4))
sns.countplot(x='Unders', data=df_5)
st.pyplot(fig5)


#fig1 = plt.figure(figsize=(10,4))
#sns.countplot(x='Unders', data=df)
#st.pyplot(fig1)
