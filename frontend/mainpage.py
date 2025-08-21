import streamlit as st
import google.generativeai as genai
from google.generativeai import types
import os


################# GEMINI API INTEGRATION LOGIC #########################

# Configure the Gemini API with the key from an environment variable.
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    # In a real-world app, you'd use Streamlit secrets for this.
    st.error("GEMINI_API_KEY environment variable not set.")
    st.stop()

genai.configure(api_key=api_key)

# The model is now an object 
model = genai.GenerativeModel('gemini-2.5-flash')

#
#
################################### FRONTEND / UI LOGIC ###################################

st.set_page_config(page_title="Vision2Summary", page_icon="🤖", layout="centered")

#webpage title
st.title("Vision2Summary")
st.markdown("Upload an image and have the analyse and produce summaries.")

#image_uplaod = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# The file uploader is now configured to accept multiple files.
uploaded_files = st.file_uploader(
    "Choose one or more PNG or JPEG files",
    type=['png', 'jpg', 'jpeg'],
    accept_multiple_files=True
)

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


