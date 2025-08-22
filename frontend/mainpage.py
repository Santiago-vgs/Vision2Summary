# Necessary imports for Streamlit, the Gemini API, and file handling.
import streamlit as st
import google.generativeai as genai
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
# The `genai` module's top-level functions now handle file uploads directly.
# The 'client = genai.Client()' line is no longer needed.

################################### FRONTEND / UI LOGIC ###################################

st.set_page_config(page_title="Vision2Summary", page_icon="🤖", layout="centered")

# Webpage title and description
st.title("Vision2Summary")
st.markdown("Upload one or more images or PDFs and have the AI analyze them.")

# The file uploader is now configured to accept multiple files.
uploaded_files = st.file_uploader(
    "Choose one or more image (PNG/JPEG) or PDF files",
    type=['png', 'jpg', 'jpeg', 'pdf'], 
    accept_multiple_files=True
)

# Resets chat history if you reload page
if "messages" not in st.session_state:
    st.session_state.messages = []

# Shows message history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# This block only runs when the user has uploaded files AND entered a prompt.
if uploaded_files and (prompt := st.chat_input("Enter your prompt here...")):
    # Display the user's message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user input to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Prepare the content for the API call
    # This list will hold the text prompt and all the file parts.
    contents_for_model = [prompt]
    
    try:
        # Loop through each uploaded file to handle it.
        for uploaded_file in uploaded_files:
            # Upload the file using the top-level genai.upload_file() function.
            # This function returns a File object that contains the URI and MIME type.
            file_upload = genai.upload_file(uploaded_file, mime_type=uploaded_file.type)
            
            # Now, you can simply append the file_upload object directly.
            # The API call will handle it correctly.
            contents_for_model.append(file_upload)

        # Display a streaming response from the model
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # --- FIX: Call generate_content() on the `model` object, not the `genai` module. ---
            for chunk in model.generate_content(contents_for_model, stream=True):
                full_response += chunk.text
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            
        # Add the AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        st.error(f"An error occurred while generating content: {e}")
        st.stop()

# Display a message to the user if no files are uploaded.
if not uploaded_files:
    st.info("Please upload files to begin the conversation.")
