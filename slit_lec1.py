import streamlit as st

#Updates Title
st.title("Plato's Podcasts 🤔 🎧 ")

st.write("BEHOLD!")

st.header("Book Buttons")
# Create buttons for each book
button_book1 = st.button("Book 1")
button_book2 = st.button("Book 2")
button_book3 = st.button("Book 3")

# Determine which button was clicked
if button_book1:
    st.write("The Dialogue of Book 1")
    button_book2 = False
    button_book3 = False

if button_book2:
    st.write("The Dialogue of Book 2")
    button_book1 = False
    button_book3 = False

if button_book3:
    st.write("The Dialogue of Book 3")
    button_book1 = False
    button_book2 = False

st.header("Checkboxes")
like = st.checkbox("Do you like this app?")
button2 = st.button("Submit")
if button2:
  if like:
    st.write("Me TOO BRO")
  else:
    st.write("Fuck you the DUUDE")

st.header("Start of the Radio Section")
animal = st.radio('What animal is your favorite?', ("Lions", "Tiger", "Bear"))

slider = st.slider("How many of this thingy", 1, 100, 10)

st.header("Text Box")
user_text = st.text_input("What you wanna eat?")

st.header("Number Input")
user_number = st.number_input("What's your favorite number?")

txt = st.text_area("Long Text Box")