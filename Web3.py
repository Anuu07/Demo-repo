import streamlit as st
st.title("Input Widgets Example")
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120, value=30)
is_happy = st.checkbox("Are you Happy")
color = st.selectbox("Choose your favourite color", ["Red","Green","Blue"])

if st.button("Submit"):
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Happy: {'Yes' if is_happy else 'No'}")
    st.write(f"Favourite color: {color}")