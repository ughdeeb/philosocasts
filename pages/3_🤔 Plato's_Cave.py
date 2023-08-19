import streamlit as st

st.title("Plato's Cave")
st.header("Enter the cave and find out what Socrates thinks!")

###Chat Section ###

#Initialize Chat History 
if "messages" not in st.session_state:
    st.session_state.messages = []


#Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Take Input from User
prompt = st.chat_input("Wusssup?")
if prompt:
    #Display user messsage 
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message 
    with st.chat_message("assistant"):
        st.markdown(response)
    #Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content":response})




### Sidebar ###
st.sidebar.header("Chat with Socrates and find out what he thinks about your favorite podcast.")

