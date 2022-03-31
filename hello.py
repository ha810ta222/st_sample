import streamlit as st
st.title("Question about you")
st.header("by ta2")
st.subheader("It's a page.")

genre = st.radio(
    "What is Your gender?",
    ('men', 'women', 'other'))

age = st.slider('How old are you?', 0, 130, 18)

name = st.text_input('What is your name', 'Your name')

st.write('Your name is' , ' ' , name , ', your gender is', ' ' , genre,  ', your age is' , ' ', age , ', OK?')