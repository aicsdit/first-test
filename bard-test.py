from bardapi import Bard
import streamlit as st

# set your __Secure-1PSID value to key
token = 'WQg4ICjZCMbMaE3SXkoWkkBrjxBodtJ6urACtwJRKvsoWlX4X-kS11WM6V-Sk7ZdJsqCbQ.'

# set your input text
input_text = "내일 아침 맛있는 아침을 먹으려고 해. 식단좀 부탁해"

# Send an API request and get a response.
bard = Bard(token=token)
response = bard.get_answer(input_text)['content']
print(response)