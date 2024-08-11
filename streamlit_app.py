import streamlit as st
from res import assist_res
from function import liteBestMatch, call_api

st.set_page_config(layout="wide")
st.title("MC Pilot")

latest_user_prompt = None
chat_col, info_col = st.columns([5, 5], gap = 'large')

if "messages" not in st.session_state:
    st.session_state.messages = []

with chat_col:
    st.subheader('Chat')
    prompt = st.chat_input("Query goes here")
    if prompt:
        latest_user_prompt = prompt
        st.session_state.messages = []
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = assist_res(prompt)

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})


with info_col:
    st.subheader('Info retrieved')
    if latest_user_prompt:
        topic = liteBestMatch(latest_user_prompt)
        st.markdown(f"Topic detected: {topic}")

        st.markdown(f"_____")

        call_api_response = call_api(liteBestMatch(topic))
        st.markdown('API Returned:')
        for key in call_api_response['results'][0].keys():
            st.markdown(f"* {key}: {call_api_response['results'][0][key]}")

