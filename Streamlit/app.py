import streamlit as st
st.title("My First Streamlit App")
st.write("Hello, Streamlit!")
st.header("Header")
st.subheader("Subheader")
st.text("Simple text")
name = st.text_input("Enter your name")
st.write("Hello", name)
if st.button("Click Me"):
    st.write("Button Clicked!")

age = st.slider("Select age", 1, 100)
st.write("Age:", age)