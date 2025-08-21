import os
import google.generativeai as genai


# The new, correct way to set the API key is using genai.configure().
# It's a best practice to load the key from an environment variable.
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")

genai.configure(api_key=api_key)

# The model is now an object you can interact with directly.
model = genai.GenerativeModel('gemini-2.5-flash')

# To generate content, you call the generate_content() method on the model object.
response = model.generate_content("What is OCR?")

# The response object is the same.
print(response.text)
