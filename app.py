import streamlit as st
import pandas as pd

data = pd.read_csv("/home/kiwitech/Downloads/Health_data2 - symptom.csv")  

st.title("Healthcare Information System")
st.write("Enter your symptoms to get relevant information.")
st.write("### Columns in the dataset:")
st.write(data.columns)  

user_input = st.text_input("Symptoms (e.g., headache, fever):")
age_input = st.text_input("Age :")
gender_input = st.selectbox("Gender :", options=["Select", "Male", "Female", "Misgender"])

if st.button("Get Information"):
    if user_input:
        symptom_column = 'symptom'  
        if symptom_column in data.columns:
            symptom_found = data[data[symptom_column].str.contains(user_input.lower(), case=False)]
            if 'age' in data.columns and age_input:
                try:
                    symptom_found = symptom_found[symptom_found['age'] == int(age_input)]
                except ValueError:
                    st.error("Please enter a valid age.")

            if 'gender' in data.columns and gender_input != "Select":
                symptom_found = symptom_found[symptom_found['gender'].str.lower() == gender_input.lower()]
            

            if not symptom_found.empty:
                st.write("### Relevant Information:")
                for _, row in symptom_found.iterrows():
                    st.write(f"**Condition:** {row['condition']}")
                    st.write(f"**Treatment:** {row['treatment']}")
            else:
                st.warning("No relevant information found. Please try a different symptom, age, or gender.")
        else:
            st.error(f"The dataset does not contain a '{symptom_column}' column.")
    else:
        st.warning("Please enter a symptom.")
