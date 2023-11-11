import os
import streamlit as st
from google.cloud import firestore

db = firestore.Client.from_service_account_json("firebaseJSON.json")

def courses():
    st.title("Courses")
    st.title('Thumbnail View')

    script_dir = os.path.dirname(os.path.abspath(__file__))
    i = 1

    while True:
        document_name = str(i)
        courses_ref = db.collection("courses").document(document_name)
        doc = courses_ref.get()

        if doc.exists:
            data = doc.to_dict()
            professor = data.get("Professor")
            course = data.get("Course")

            image_path = os.path.join(script_dir, f'../../images/courseIcon.png')

            st.image(image_path, caption=f"{course} - {professor}", width=150)

            i += 1
        else:
            break
