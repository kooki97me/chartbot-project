import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd


def display_matplotlib_chart(
    x_data,
    y_data,
    title="Matplotlib Chart",
    x_label="X-axis",
    y_label="Y-axis",
    legend_label="Data",
):
    fig, ax = plt.subplots()

    ax.plot(
        x_data,
        y_data,
        label=legend_label
    )

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend()

    st.pyplot(fig)
    plt.close(fig)


def display_seaborn_scatterplot(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    hue_col: str = None,
    title="Seaborn Scatter Plot",
):
    fig, ax = plt.subplots()

    sns.scatterplot(
        data=df,
        x=x_col,
        y=y_col,
        hue=hue_col,
        ax=ax,
    )

    ax.set_title(title)

    st.pyplot(fig)
    plt.close(fig)


def display_plotly_barchart(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title="Plotly Interactive Bar Chart",
):
    if (
        df[x_col].dtype == "object"
        or df[x_col].dtype.name == "category"
    ):
        chart_df = df
    else:
        chart_df = (
            df.groupby(
                x_col,
                as_index=False
            )[y_col]
            .sum()
        )

    fig = px.bar(
        chart_df,
        x=x_col,
        y=y_col,
        title=title,
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
