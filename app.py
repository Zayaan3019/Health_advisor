import streamlit as st
from chatbot import HealthChatbot
import os

# Load API key securely
API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize chatbot
chatbot = HealthChatbot(api_key=API_KEY)

# Streamlit app layout
st.set_page_config(page_title="Personal Health Assistant", layout="wide")
st.title("🩺 Personal Health Assistant Chatbot")

# Chat interface
if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.text_input("Ask me anything about your health:", key="input")
if st.button("Send"):
    if user_input:
        response = chatbot.generate_response(user_input, st.session_state["messages"])
        st.session_state["messages"].append({"user": user_input, "bot": response})
        st.text_area("Chat History", value="\n".join(
            f"User: {msg['user']}\nBot: {msg['bot']}" for msg in st.session_state["messages"]
        ), height=300)

st.sidebar.title("About")
st.sidebar.info("This chatbot provides general health advice. Please consult a professional for medical emergencies.")
