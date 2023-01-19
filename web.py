import streamlit as st

from helper_functions import get_todos, write_todos

st.title('My ToDo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')

st.checkbox('Learn AI')
