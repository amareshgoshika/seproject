import streamlit as st
from google.cloud import firestore

db = firestore.Client.from_service_account_json("firebaseJSON.json")

def newFaculty():
    st.title("Register New Faculty Member")

    fullName = st.text_input("Full Name:")
    lid = st.text_input("Lamar ID:")
    dob = st.text_input("DOB:")
    gender = st.radio("Select Gender", ["Male", "Female", "Other"])
    email = st.text_input("Email:")
    phone = st.text_input("Phone:")
    address = st.text_input("Address:")
    designation = st.text_input("Designation:")
    notes = st.text_input("Notes:")
    if st.button("Register"):
        doc_ref = db.collection("facultyData").document(lid)
        doc = doc_ref.get()
        data = doc.to_dict()
        data_to_add = {
            "fullName": fullName,
            "lid": lid,
            "dob": dob,
            "gender": gender,
            "email": email,
            "phone": phone,
            "address": address,
            "designation": designation,
            "notes": notes,
        }
        doc_ref.set(data_to_add)
        st.success(f"Faculty Registered Successful")


