import streamlit as st
from chatbot.engine import respond
from charts.visualize import display_chart

st.title("Chatbot with Analytics")

user_input = st.text_input("You:", "")

if user_input:
    response = respond(user_input)
    st.write("Bot:", response)
    display_chart()
