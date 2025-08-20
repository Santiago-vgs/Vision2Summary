import streamlit as st

st.set_page_config(page_title = "Vision2Summary")

st.title("Vision2Summary")

# Use a 'with' block to create a form container.
# The key is required and must be unique.
with st.form("my_form"):
    # Accepts user upload
    image_upload = st.file_uploader(label = "Upload your image: ")

    # Takes multiple lines of user input
    user_input = st.text_area("Enter instructions")
    
    # Place the submit button inside the form
    submit = st.form_submit_button(label="Submit")

# Check if the submit button was clicked
if submit:
    # This code will only run when the button is pressed
    if image_upload is not None and user_input:
        st.write("Processing your request...")
        st.write(f"Image uploaded: {image_upload.name}")
        st.write(f"User instructions: {user_input}")
    else:
        st.write("Please upload an image and enter instructions.")

