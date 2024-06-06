
from dotenv import load_dotenv
load_dotenv()   ## load all the enviroment variable

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini pro model and get responsese
model=genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(img):
    response=model.generate_content(img)
    return response.text

## initialize our steamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

input=st.text_input("Input:-",key="input")
submit=st.button("Submit")

##when submit buttion click
if submit:
    response=get_gemini_response(input)
    st.subheader("the respose is ")
    st.write(response)
