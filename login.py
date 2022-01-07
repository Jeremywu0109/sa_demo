import streamlit as st
import numpy as np
import webbrowser
import time
st.balloons()
def main():
    st.title("This is the app from Group 2")
    menu = ["Login","SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)
    url = 'http://localhost:8501'
    if choice == "Login":
        st.sidebar.subheader("Login Phase")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.button("Login"):
            if username == "" and password == "":
                st.error("You need more info")
            elif username != "" and password != "":
                st.success("Logged In as {}".format(username))
                webbrowser.open(url)
                st.balloons()
    elif choice == "SignUp":
        st.sidebar.subheader("Create Account")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.button("SignUp") and username == "":
            st.error("You need more info")
            if username != "" and password != "":
                st.success("Logged In as {}".format(username))

if __name__ == '__main__':
    main()