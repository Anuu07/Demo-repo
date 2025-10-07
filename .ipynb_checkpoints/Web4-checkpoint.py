import streamlit as st
st.title("Addition of Two Numbers")
num1 = st.number_input("Enter the first number",value=0.0)
num2 = st.number_input("Enter the second number",value=0.0)

if st.button("Calculate Sum"):
    sum_result = num1 + num2
    st.success(f"The sum of {num1} and {num2} is: {sum_result}")

    st.write(f"Current first number: {num1} ")
    st.write(f"Current second number: {num2} ")
    st.write(f"Current sum: {num1 + num2} ")
