# !pip install bardapi
import streamlit as st
from bardapi import Bard

token = 'WQg4ICjZCMbMaE3SXkoWkkBrjxBodtJ6urACtwJRKvsoWlX4X-kS11WM6V-Sk7ZdJsqCbQ.'

st.title("Bard")

with st.form("myform"):
    user_input = st.text_input("Prompt")
    submit = st.form_submit_button("제출")

if submit and user_input:
    st.write(user_input)


bard = Bard(token=token)
response = bard.get_answer(user_input)['content']

st.write(response)