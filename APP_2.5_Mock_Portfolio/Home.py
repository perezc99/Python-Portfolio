import streamlit as st
import pandas

df = pandas.read_csv("data.csv")

st.set_page_config(layout="wide")
st.title("Amazing Company")

comp_desc = """
    Pulvinar pellentesque habitant morbi tristique senectus et netus et malesuada. Id cursus metus aliquam eleifend 
    mi in. Quis varius quam quisque id diam vel. Id cursus metus aliquam eleifend mi. Risus sed vulputate odio ut enim 
    blandit volutpat maecenas volutpat. Tellus at urna condimentum mattis pellentesque id nibh tortor id. Netus et 
    malesuada fames ac turpis egestas integer. Id aliquet lectus proin nibh nisl condimentum id. Sed elementum tempus 
    egestas sed. In est ante in nibh mauris cursus mattis molestie. 
"""

st.write(comp_desc)

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(f"{row['role']}")
        st.image("images/" + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(f"{row['role']}")
        st.image("images/" + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(f"{row['role']}")
        st.image("images/" + row['image'])