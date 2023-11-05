import streamlit as st

def newStudent():
    st.title("Register New Student")

    # user_type = st.radio("Select User Type", ["Admin", "Faculty", "Student"])
    fullName = st.text_input("Full Name:")
    dob = st.text_input("DOB:")
    gender = st.radio("Select Gender", ["Male", "Female", "Other"])
    email = st.text_input("Email:")
    phone = st.text_input("Phone:")
    address = st.text_input("Address:")
    designation = st.text_input("Designation:")
    notes = st.text_input("Notes:")
    st.button("Login")
