"""Financial Advisor AI Chatbot

This module implements a Streamlit-based chatbot that provides financial advice using
the Google Gemini AI model. The chatbot maintains conversation history and provides
responsive, unbiased financial guidance.

Dependencies:
    - streamlit
    - google.genai
"""

import streamlit as st
from google import genai
from google.genai import types

# Initialize Gemini API with authentication
gemini_key = "AIzaSyBd80tDTtL5Z5s5GK-Qfz1Rt6oPWr-GXjQ"
client = genai.Client(api_key=gemini_key)

def get_financial_advice(user_input: str) -> str:
    """Generate financial advice response using Gemini AI model.

    Args:
        user_input (str): The user's financial question or query

    Returns:
        str: AI-generated financial advice or error message if request fails

    The function uses a system instruction to ensure the AI provides fair,
    transparent and privacy-conscious financial advice.
    """
    sys_instruct = """
    You are a financial advisor AI. Provide investment advice while prioritizing fairness,
    transparency, and privacy. Ensure recommendations are unbiased and explainable,prefer to answer questions some concisely except user demanded to answer in detail(maximum = 60 lines).  
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction=sys_instruct,
                temperature=0.3,
            ),
            contents=[user_input]
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit UI
st.title("Financial Advisor AI")
st.write("Ask me anything about finance and investments!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's your question?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        response = get_financial_advice(prompt)
        st.markdown(response)
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})