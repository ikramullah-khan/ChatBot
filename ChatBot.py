import google.generativeai as genai
import streamlit as st
GOOGLE_API_KEY = "AIzaSyD01EQbq91h8f8namcHJJXaSttmr5wGY4k"

genai.configure(api_key=GOOGLE_API_KEY)

# Model initiate

model = genai.GenerativeModel("gemini-1.5-flash")

def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

#streamlit interface
st.set_page_config(page_title="Simple ChatBot", layout="centered")
st.title("Simple ChatBot")
st.write("It uses GOOGLE API KEY")

#user_input = input("Enter your prompt = ")
#output = getResponseFromModel(user_input)

#print(output)

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000)
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response =get_chatbot_response(user_input)
            st.write(response)
        else:
            st.warnig("Please enter a prompt") 