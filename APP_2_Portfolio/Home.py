import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)


with col1:
    st.image("images/photo.png")


with col2:
    st.title("Cesar Antonio Perez Oloroso")
    content = "Hello World"
    st.info(content)

st.subheader("Below are my coding projects. Feel free to contact me!")

col3, empty_col, col4 = st.columns([1.25, 0.1, 1.25])

df = pandas.read_csv("data.csv", sep=";")

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


