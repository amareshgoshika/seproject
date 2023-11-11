import streamlit as st
from google.cloud import firestore

db = firestore.Client.from_service_account_json("firebaseJSON.json")

def addCourse():
    st.title("Add New Course")

    courseName = st.text_input("Course:")
    professor = st.text_input("Professor")
    startDate = st.text_input("Start Date:")
    if st.button("Register"):
        doc_ref = db.collection("courses").document("3")
        doc = doc_ref.get()
        data = doc.to_dict()
        data_to_add = {
            "Course": courseName,
            "Professor": professor,
            "StartDate": startDate,
        }
        doc_ref.set(data_to_add)
        st.success(f"Course Added Successful")


