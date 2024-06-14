import streamlit as st
import google.generativeai as genai


st.title("Zen Panda")



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


genai.configure(api_key=st.secrets["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction="Give responses like you are a therapist, give the answer in less than 45 words, demonstrate curiosity and show support being non judgemental",)
chat = model.start_chat(history=st.session_state.messages)


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_response(user):
    response = chat.send_message(user)
    return response


# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    bot = get_response(prompt)
    response = f"{bot}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
