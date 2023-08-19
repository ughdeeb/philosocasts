import streamlit as st

st.title("Plato's Cave")
st.text("Talk with Socrates yourself and ask him philosophical questions about your podcast!")
with st.chat_message(name="assistant", avatar= "🧔🏼"):
    st.write("Hello I am Socrates! ")



st.sidebar.header("Chat with Socrates and find out what he thinks about your favorite podcast.")