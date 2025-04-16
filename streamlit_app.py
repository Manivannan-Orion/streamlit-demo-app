import os
import sys
import time

import streamlit as st


with st.sidebar:
    st.title('Data Upload')
    st.write('This chatbot is created using the open-source Llama 2 LLM model from Meta.')
    st.success('API key already provided!', icon='✅')

# Title
st.title("🔮 Support Helpdesk")
intro = "Hey! I am Pre IT Support chat, your assistant for finding the best answer to your issues. Let's get started!"
st.markdown(intro)



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.greetings = False


if prompt := (st.chat_input("Please ask your problem")):
    # Display user message in chat message container
    with st.chat_message("user"):
        # st.markdown(prompt)
        st.write(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    prompt = prompt.replace('"', "").replace("'", "")

    if prompt != "":
        query = prompt.strip().lower()
        print(f"user query is {query}")

        response = """
For more advanced formatting, Streamlit introduces `st.latex` for rendering mathematical expressions and `st.write`, which acts as a Swiss Army knife, automatically formatting its input based on the data type. This flexibility allows developers to present data and information in a structured and engaging way, catering to a wide range of application needs. Streamlit's approach to text formatting is designed to be intuitive, enabling developers to create rich text elements with minimal effort.

        """
        with st.chat_message("assistant"):
            st.write(response)
            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )