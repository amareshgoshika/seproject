import streamlit as st
from google.cloud import firestore
from admin.welcome import welcome

db = firestore.Client.from_service_account_json("firebaseJSON.json")

def login_page():
    st.title("Welcome to A2S")
    st.write("Login to get acess to A2S")

    user_type = st.radio("Select User Type", ["Admin", "Faculty", "Student"])
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    doc_ref = db.collection("loginTable").document(user_type)
    doc = doc_ref.get()
    data = doc.to_dict()

    if st.button("Login"):
        if user_type == "Admin":
            # Add logic for user login here
            if username == data.get("username") and password == data.get("password"):
                st.session_state.logged_in = True
                st.session_state.user = "Admin"
                st.experimental_rerun()
            else:
                st.error("Incorrect username or password for Admin.")
        elif user_type == "Faculty":
            # Add logic for admin login here
            if username == data.get("username") and password == data.get("password"):
                st.session_state.logged_in = True
                st.session_state.user = "Faculty"
                st.experimental_rerun()
            else:
                st.error("Incorrect username or password for Faculty.")
        elif user_type == "Student":
            # Add logic for admin login here
            if username == data.get("username") and password == data.get("password"):
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
        from admin.pages import newFaculty
        from admin.pages import newStudent
        from admin.pages import viewFaculty
        from admin.pages import viewStudent
        from admin.pages import courses
        from admin.pages import addCourse
        selected_tab = st.sidebar.radio("", ["Welcome", "New Faculty", "New Student", "View Faculty", "View Student", "Courses", "Add Course"])

        if selected_tab == "Welcome":
            welcome()
        elif selected_tab == "New Faculty":
            newFaculty.newFaculty()
        elif selected_tab == "New Student":
            newStudent.newStudent()
        elif selected_tab == "View Faculty":
            viewFaculty.viewFaculty()
        elif selected_tab == "View Student":
            viewStudent.viewStudent()
        elif selected_tab == "Courses":
            courses.courses()
        elif selected_tab == "Add Course":
            addCourse.addCourse()

    elif st.session_state.user == "Faculty":
        from admin.pages import newFaculty
        selected_tab = st.sidebar.radio("Select Page", ["Welcome", "New Faculty"])

        if selected_tab == "Welcome":
            welcome()
        elif selected_tab == "New Faculty":
            newFaculty.newFaculty()

    elif st.session_state.user == "Student":
        from student.pages import page1
        selected_tab = st.sidebar.radio("Select Page", ["Welcome", "Courses", "Attendance"])

        if selected_tab == "Welcome":
            welcome()
        elif selected_tab == "Attendance":
            page1.page1()
else:
    login_page()
