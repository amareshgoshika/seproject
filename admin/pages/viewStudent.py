import streamlit as st
from google.cloud import firestore

db = firestore.Client.from_service_account_json("firebaseJSON.json")

def viewStudent():
    st.title("View Student Data")

    # Access the Firestore collection
    collection_ref = db.collection("studentData")

    # Get all documents in the collection
    docs = collection_ref.stream()

    # Initialize an empty list to store the data for each document
    all_data = []

    for doc in docs:
        data = doc.to_dict()

        # Append the data for each document to the list
        all_data.append(data)

    # Display the data as a table with rows
    if all_data:
        # Get the keys from the first document to use as table headers
        headers = all_data[0].keys()

        # Create a list of lists for the table data
        table_data = [list(data.values()) for data in all_data]

        # Display the table with headers and data
        st.table([headers] + table_data)
    else:
        st.write("No data found in the collection.")

if __name__ == "__main__":
    viewStudent()
