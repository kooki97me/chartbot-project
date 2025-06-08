import streamlit as st
import matplotlib.pyplot as plt

def display_chart():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 4, 9], label="Example")
    ax.set_title("Example Chart")
    ax.legend()
    st.pyplot(fig)
