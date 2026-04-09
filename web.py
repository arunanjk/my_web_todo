import streamlit as st
import functions_todo as ft
import os


todos = ft.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]+ "\n"
    todos.append(todo)
    ft.write_todos(todos)




todos = ft.get_todos()
st.title("My Todo App")
st.subheader("This is my todo app")

for i,j in enumerate(todos):
    checkbox = st.checkbox(j,key = j)
    if checkbox:
        todos.pop(i)
        ft.write_todos(todos)
        del st.session_state[j]
        st.rerun()
s = st.text_input(label="",placeholder="Enter a todo",
                  on_change = add_todo, key = 'new_todo')
st.session_state