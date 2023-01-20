import streamlit as st

from helper_functions import get_todos, write_todos


to_dos = get_todos()


def add_todo():
    to_do = f"{st.session_state['new_todo']}\n"
    to_dos.append(to_do)
    write_todos(to_dos)


st.title('My ToDo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')

for index, to_do in enumerate(to_dos):
    checkbox = st.checkbox(to_do, key=to_do)
    if checkbox:
        to_dos.pop(index)
        write_todos(to_dos)
        del st.session_state[to_do]
        st.experimental_rerun()

st.text_input(label='Enter more Todos', placeholder='Add new to do', on_change=add_todo, key='new_todo')
