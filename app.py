import streamlit as st

st.write("This app gives back the maximum of 3 numbers")
st.header("Please input 3")

number_1 = st.number_input("Enter the first number")
number_2 = st.number_input("Enter the second number")
number_3 = st.number_input("Enter the third number")

numbers = [number_1, number_2, number_3]

st.header("The max number is ")
st.write(max(numbers))
