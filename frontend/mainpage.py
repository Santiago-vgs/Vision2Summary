import streamlit as st

st.title("VIsion2Summary")

image_uplaod = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

with st.form("my_text_form"):
    # Text input widget
    user_text = st.text_area("Enter your text:")

    # Submit button for the form
    submit_button = st.form_submit_button("Submit Text")

# Process the submitted data
if submit_button:
    if user_text:
        st.success(f"You submitted: {user_text}")
    else:
        st.warning("Please enter some text before submitting.")


