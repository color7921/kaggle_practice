import streamlit as st
import time
prompt = st.chat_input("입력하세요")
msg = st.container()

if 'message' not in st.session_state:
    st.session_state['message'] = []

if prompt:
    st.session_state['message'].append({'type':'user','text':f"{prompt}"})
    st.session_state['message'].append({'type':'assistant','text':f"{prompt}? 무슨 말인지 모르겠네!"})

    #session_state = []
    #Prompt : 안녕
    #session_state = [{type:"user",text:"안녕"}]
    #AI : 안녕? 무슨 말인지 모르겠네!
    #session_state = [{type:"user",text:"안녕"},{type:"assistant",text:"안녕? 무슨 말인지 모르겠네"}]

    for i in st.session_state['message']:
        if i['type'] == "user":
            msg.chat_message("user").write(i['text'])
        else:
            msg.chat_message("assistant").write(i['text'])