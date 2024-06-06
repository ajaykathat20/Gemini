from dotenv import load_dotenv
load_dotenv()   ## load all the enviroment variable

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini pro model and get responsese
model=genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input,img):
    if input !="":
        response=model.generate_content([input,img])
    else:
        response=model.generate_content(img)
    return response.text

## initialize our steamlit app
st.set_page_config(page_title="Gemini Image  Demo")
st.header("Gemini Application")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

input=st.text_input("Input prompt:-",key="input")

submit=st.button("Tell me about the image")

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)

