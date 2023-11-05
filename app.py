import streamlit as st
import os
import sys

from admin.welcome import welcome
from faculty.faculty_dashboard import faculty_dashboard

# Define the login page
def login_page():
    st.title("Welcome to A2S")

    user_type = st.radio("Select User Type", ["Admin", "Faculty", "Student"])
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if st.button("Login"):
        if user_type == "Admin":
            # Add logic for user login here
            if username == "admin" and password == "password":
                st.session_state.logged_in = True
                st.session_state.user = "Admin"
                st.experimental_rerun()
            else:
                st.error("Incorrect username or password for Admin.")
        elif user_type == "Faculty":
            # Add logic for admin login here
            if username == "faculty" and password == "password":
                st.session_state.logged_in = True
                st.session_state.user = "Faculty"
                st.experimental_rerun()
            else:
                st.error("Incorrect username or password for Faculty.")
        elif user_type == "Student":
            # Add logic for admin login here
            if username == "student" and password == "password":
                st.session_state.logged_in = True
                st.session_state.user = "Student"
                st.experimental_rerun()
            else:
                st.error("Incorrect username or password for Student.")
        else:
            st.error("Please select a valid User Type.")

# Main app logic
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    if st.session_state.user == "Admin":
        from admin.pages import page1
        selected_tab = st.sidebar.radio("Select Page", ["Welcome", "Page 1"])

        if selected_tab == "Welcome":
            welcome()
        elif selected_tab == "Page 1":
            page1.page1()
    elif st.session_state.user == "Faculty":
        from faculty.pages import page1
        selected_tab = st.sidebar.radio("Select Page", ["Welcome", "Page 1"])

        if selected_tab == "Welcome":
            welcome()
        elif selected_tab == "Page 1":
            page1.page1()
    elif st.session_state.user == "Student":
        from student.pages import page1
        selected_tab = st.sidebar.radio("Select Page", ["Welcome", "Page 1"])

        if selected_tab == "Welcome":
            welcome()
        elif selected_tab == "Page 1":
            page1.page1()
else:
    login_page()
