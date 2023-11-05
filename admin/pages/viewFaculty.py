import streamlit as st

def viewFaculty():
    # Sample data as a list of dictionaries
    data = [
        {"Name": "Alice", "Age": 25, "City": "New York"},
        {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
        {"Name": "Charlie", "Age": 22, "City": "Chicago"},
        {"Name": "David", "Age": 28, "City": "San Francisco"},
    ]

    # Display the list data as a table
    st.table(data)

