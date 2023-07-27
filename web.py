import streamlit as st
import function


todos=function.get()
def add_todo():
    todo=st.session_state["new_todo"] + '\n'
    todos.append(todo)
    function.wrt(todos)


st.title("My todo APP")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    print(checkbox)
    if checkbox:
        todos.pop(index)
        function.wrt(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a todo: ", placeholder="Add new todo...",on_change=add_todo,key='new_todo')

#st.session_state