import streamlit as st

st.title("Lecture 2: Layouts and Images")
st.sidebar.header("Options")
st.sidebar.image("assets/plato.png", width = 100)

def clean_text(text):
    text = text.replace("\n", " ").strip().upper()
    return text

#Text Area
text = st.sidebar.text_area("Past Text Here")
button1 = st.sidebar.button("Clean Text")
if button1: 
    col1, col2 = st.columns(2)
    col1_expander = col1.expander("Expand")
    col1.header("Original Text")
    col1.write(text)
    
    col2.header("Cleaned Text")
    clean = clean_text(text)
    col2.write(clean)



