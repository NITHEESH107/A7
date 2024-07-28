import streamlit as st 
# title-
st.title("User Information Collector")
st.write("Enter your information below:")

# Input widgets for user data
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
# Button to submit the data
if st.button("Submit"):
    # Append the data to a CSV file
    with open("user_data.csv", "a") as f:
        f.write(f"{name},{age}\n")
    st.success("Data submitted successfully!")
    import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Load the data for visualization
try:
    data = pd.read_csv("user_data.csv", header=None, names=["Name", "Age"])
    
    # Display the data table
    st.write("### User Data")
    st.dataframe(data)
    
    # Display the histogram
    st.write("### Age Distribution")
    fig, ax = plt.subplots()
    ax.hist(data["Age"], bins=10, edgecolor='black')
    ax.set_xlabel("Age")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
    
except FileNotFoundError:
    st.warning("No data available yet. Please submit your information.")
    

