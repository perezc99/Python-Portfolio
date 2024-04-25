import streamlit as st
from send_email import send_email


st.header("Contact Me")
with st.form(key="email_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First Name")
    with col2:
        last_name = st.text_input("Last Name")
    user_email = st.text_input("Your Email Address")
    user_raw_msg = st.text_area("Your Message")
    user_message = f"""\
Subject: Email from {first_name} {last_name}

From: {user_email}
{user_raw_msg}
"""
    btn = st.form_submit_button("Submit")
    if btn:
        send_email(user_message)
        st.info("Your email was sent successfully!")