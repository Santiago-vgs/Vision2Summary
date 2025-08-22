# Necessary imports for Streamlit, the Gemini API, and file handling.
import streamlit as st
import google.generativeai as genai
from google.generativeai import types
import os

################# GEMINI API INTEGRATION LOGIC #########################

# Configure the Gemini API with the key from an environment variable.
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    # In a real-world app, you'd use Streamlit secrets for this.
    st.error("GEMINI_API_KEY environment variable not set. Please set it and rerun the app.")
    st.stop()

genai.configure(api_key=api_key)

# The model is now an object 
model = genai.GenerativeModel('gemini-2.5-flash')

################################### FRONTEND / UI LOGIC ###################################

st.set_page_config(page_title="Vision2Summary", page_icon="🤖", layout="centered")

# Webpage title and description
st.title("Vision2Summary")
st.markdown("Upload an image and have the AI analyze it and produce a summary.")

# The file uploader is now configured to accept multiple files.
uploaded_files = st.file_uploader("Choose one or more PNG or JPEG files", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

# Resets chat history if you reload page
if "messages" not in st.session_state:
    st.session_state.messages = []

# Shows message history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Enter a prompt")
if prompt:
    ##show user message, in container
    with st.chat_message("user"):
        st.markdown(prompt)
    #add user input to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

