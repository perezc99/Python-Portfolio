import streamlit as st
import functions

todos = functions.get_todos()

# st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To Do App")
st.subheader("To Do List: ")
st.write("This app increases productivity!")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a to do",
              on_change=add_todo, key="new_todo")
