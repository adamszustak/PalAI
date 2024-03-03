import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


class Streamlit_app:
    def __init__(self):
        self._initialize_env()

    def _initialize_env(self):
        st.title("Friendly Ken Chatbot")
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def _display_msg(self, role, prompt):
        with st.chat_message(role):
            st.markdown(prompt)
            if role == "assistant":
                with st.expander("See explanation"):
                    st.write(
                        """
                            The chart above shows some numbers I picked for you.
                            I rolled actual dice for these, so they're *guaranteed* to
                            be random.
                        """
                    )

    def display_msg_history(self):
        for message in st.session_state.messages:
            self._display_msg(message["role"], message["prompt"])

    def display_current_msg(self, role, prompt):
        self._display_msg(role, prompt)

    def add_msg_to_history(self, role, prompt):
        st.session_state.messages.append({"role": role, "prompt": prompt})

    def clear_history(self):
        st.session_state.messages = []


load_dotenv()
app_instance = Streamlit_app()
if prompt := st.chat_input("What is up?"):
    app_instance.display_msg_history()
    app_instance.display_current_msg("user", prompt)
    app_instance.add_msg_to_history("user", prompt)

    response = f"Echo: {prompt}"
    app_instance.display_current_msg("assistant", response)
    app_instance.add_msg_to_history("assistant", response)
