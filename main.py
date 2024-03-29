import streamlit as st
import pandas #pandas allows to import csv data


primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width = 900)
with col2:
    st.title("Amir Alekperov")
    content = """
    Hello! My name is Amir! I am a Python developer with some FullStack and DevOps background. Although my primary background is petroleum engineering, however I was always interested in everything related to computers and, especially coding, web and app development. 
    I am welcoming you to my personal portfolio webpage, hope you like it and learn something new from it!    
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python! Feel free to contact me should you have any questions and offers!
"""

st.write(content2)

col3, empty_col,  col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep = ";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
    