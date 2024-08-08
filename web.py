import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("To-do App")
st.subheader("General tasks")
st.write("Create and complete to-do items below.")

st.text_input(label="",
              label_visibility="collapsed",
              placeholder="Add new todo item...",
              on_change=add_todo,
              key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

