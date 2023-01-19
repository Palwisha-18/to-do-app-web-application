import streamlit as st

from helper_functions import get_todos, write_todos

to_dos = get_todos()

st.title('My ToDo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')

for to_do in to_dos:
    st.checkbox(to_do)

st.text_input(label='', placeholder='Add new to do')
