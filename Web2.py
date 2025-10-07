import streamlit as st 
st.title("My First Streamlit App")

name=st.text_input("Enter your name ")
email=st.text_input("Enter your email")

if st.button("Say Hello"):
    if name:
        st.write(f"Hello,{name}!")
    else:
        st.write("Please enter your name.")
        