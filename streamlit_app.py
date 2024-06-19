import streamlit as st
import pandas as pd
from datetime import datetime

# Title of the app

st.title("Submit Questions About Trace")

st.caption("Hello! This form is used to collect your questions for Trace as we are developing a Chatbot. Thanks for your input.")

# Collect question related to the order
question = st.text_area("Enter your question about Trace (required):")

# Collect order number
order_number = st.text_input("Enter your order number (if applicable):", value="")

# Collect question related to the order
# type = st.radio(
#     "Select whether your question is about sourcing or delivery:",
#     [
#         "Sourcing",
#         "Delivery",
#         "Not Specific"
#     ],
#     index = 2
# )

# Button to submit the form
if st.button("Submit"):
    # if order_number and type and question:
    if question:
        # Load existing data
        try:
            data = pd.read_csv('submissions.csv')
        except FileNotFoundError:
            data = pd.DataFrame(columns=['SubmissionTime', 'Order Number', 'Type', 'Question'])

        # Append new data
        submission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[submission_time, order_number, type, question]], columns=['SubmissionTime', 'Order Number', 'Type', 'Question'])
        data = pd.concat([data, new_data], ignore_index=True)
        
        # Save updated data
        data.to_csv('submissions.csv', index=False)

        st.success("Thank you for submitting questions!")
        print(order_number, type, question)
        # Here you can add code to process/store the collected data
    else:
        st.error("Please fill in all fields before submitting.")
