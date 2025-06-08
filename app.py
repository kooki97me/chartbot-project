import streamlit as st
from chatbot.engine import respond_spacy, respond_openai
from charts.visualize import display_matplotlib_chart, display_seaborn_scatterplot, display_plotly_barchart
import pandas as pd

st.title("Chatbot with Analytics")

# Sidebar for API Key and engine selection
st.sidebar.header("Chatbot Settings")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
use_openai_cb = st.sidebar.checkbox("Use OpenAI for responses", value=False)

# Prepare sample data for charts
chart_df = pd.DataFrame({
    'x_numeric': [1, 2, 3, 4, 5, 6, 7, 8],
    'y_values_A': [10, 12, 15, 13, 17, 18, 20, 19],
    'y_values_B': [5, 7, 6, 8, 7, 9, 10, 8],
    'category': ['Alpha', 'Beta', 'Alpha', 'Gamma', 'Beta', 'Alpha', 'Gamma', 'Beta']
})

user_input = st.text_input("You:", "")

if user_input: # This will trigger on Enter or if text_input loses focus with content
    if use_openai_cb:
        if openai_api_key:
            response = respond_openai(user_input, openai_api_key)
        else:
            response = "Please enter your OpenAI API Key in the sidebar to use the OpenAI engine."
    else:
        response = respond_spacy(user_input)
    st.write("Bot:", response)

st.header("Analytics Visualizations")
chart_type = st.selectbox(
    "Select Chart Type:",
    ("Matplotlib Line Plot", "Seaborn Scatter Plot", "Plotly Bar Chart")
)

if st.button(f"Show {chart_type}"):
    if chart_type == "Matplotlib Line Plot":
        display_matplotlib_chart(x_data=chart_df['x_numeric'], y_data=chart_df['y_values_A'],
                                 title="Matplotlib: Numeric X vs Y Values A", legend_label="Y Values A")
    elif chart_type == "Seaborn Scatter Plot":
        display_seaborn_scatterplot(df=chart_df, x_col='x_numeric', y_col='y_values_A', hue_col='category',
                                    title="Seaborn: Scatter of Y Values A by Category")
    elif chart_type == "Plotly Bar Chart":
        # For bar chart, let's aggregate y_values_B by category
        aggregated_df = chart_df.groupby('category')['y_values_B'].sum().reset_index()
        display_plotly_barchart(df=aggregated_df, x_col='category', y_col='y_values_B',
                                title="Plotly: Sum of Y Values B by Category")
