import streamlit as st
st.title("Question about you")
st.header("by ???")
st.text("It's a page.")

genre = st.radio(
    "What is Your gender?",
    ('men', 'women', 'other'))

age = st.slider('How old are you?', 0, 130, 18)

name = st.text_input('What is your name', 'Your name')

d = st.date_input(
    "When is your birth day?", 
    datetime.date(2022, 3, 25))


