import streamlit as st
import numpy as np
import time

def main():
    st.title("This is the app from Group 2")
    menu = ["Login","SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Login":
        st.sidebar.subheader("Login Phase")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.button("Login") and username == "":
            st.error("You need more info")
        elif username != "":
            st.success("Logged In as {}".format(username))
    elif choice == "SignUp":
        st.sidebar.subheader("Create Account")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.button("SignUp") and username == "":
            st.error("You need more info")
        elif username != "" and password != "":
            st.success("Logged In as {}".format(username))
    st.balloons()

if __name__ == '__main__':
    main()