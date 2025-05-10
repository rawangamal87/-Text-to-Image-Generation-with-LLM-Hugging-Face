import streamlit as st

st.title("Text to Image Generator")
prompt = st.text_input("Enter your prompt:")
if st.button("Generate"):
    # Your model code here
    st.image(generated_image)
