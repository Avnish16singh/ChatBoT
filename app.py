import streamlit as st  # for UI
import os  # to get the environment variable into the application
from dotenv import load_dotenv
import google.generativeai as genai

# Loading all the environment variables
load_dotenv()

# GenAI configuration of API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initializing the model
model = genai.GenerativeModel('gemini-pro')

# Defining a function
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.candidates[0].content.parts[0].text

# Setting up Streamlit app
st.set_page_config(
    page_title="Gemini Pro Q&A",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Setting up header
st.header("Chat AI")

# Adding a sidebar
st.sidebar.title("History")

def add_to_history( text_input):
    st.session_state.history.append({
        'text_input': text_input
    })

# Input
question = st.text_input("Question")

if st.sidebar.button("Save Input"):
    add_to_history(question)

# Submit
if st.button("Submit"):
    response = get_gemini_response(question)
    st.write("**You:**", question)
    st.write("**Gemini:**", response)
