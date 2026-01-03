"""Python module showcasing client side which runs the streamlit front-end showcasing the chat history message"""

# PS this code is shit and I dont like how its structured any advice?
import requests
import streamlit as st

st.title("FastAPI Chatbot")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Write your prompt in the field"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        response = requests.get(
            "http://localhost:8000/generate/text", params={"prompt": prompt}
        )
        response.raise_for_status()
        full_response = response.text

        with st.chat_message("assistant"):
            st.markdown(full_response)

        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )

    except Exception as e:
        st.error(f"Failed to connect to FastAPI: {e}")
