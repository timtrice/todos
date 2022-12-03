import streamlit as st
from functions import get_todos, write_todos

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)


todos = get_todos()

st.title("My TODO App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)

    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label='Add a todo',
              placeholder='Add a new todo...',
              on_change=add_todo,
              key='new_todo')
