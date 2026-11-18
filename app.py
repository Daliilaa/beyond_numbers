import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from analysis import (
    FACTORS,
    load_data,
    get_country_data,
    calculate_summary,
    calculate_all_correlations,
    create_scatter_plot
)


# Page configuration
st.set_page_config(
    page_title="Beyond Numbers",
    page_icon="🌍",
    layout="wide"
)


# Load data
df = load_data()


# Application header
st.title("Beyond Numbers")

st.subheader("What makes people happy?")

st.write(
    "Explore the relationship between economic "
    "and social factors and global life satisfaction."
)


# User selections
left, right = st.columns(2)

with left:

    country = st.selectbox(
        "Select a country",
        sorted(df["country"].dropna().unique())
    )

with right:

    factor = st.selectbox(
        "Explore a factor",
        list(FACTORS.keys())
    )


# Retrieve statistical results
selected_country = get_country_data(df, country)

summary = calculate_summary(df)

correlations = calculate_all_correlations(df)

score = selected_country["happiness"].iloc[0]

average = summary["mean"]

correlation = correlations[factor]


# Display metrics
col1, col2, col3 = st.columns(3)

col1.metric(
    "Happiness score",
    f"{score:.2f}"
)

col2.metric(
    "Country average",
    f"{average:.2f}"
)

col3.metric(
    "Pearson correlation",
    f"{correlation:.2f}" if pd.notna(correlation) else "N/A"
)


# Display scatter plot
fig = create_scatter_plot(df, country, factor)

st.pyplot(fig)

plt.close(fig)


# Display correlations
st.subheader("Factors associated with happiness")

st.bar_chart(correlations)


# Display descriptive statistics
with st.expander("Descriptive statistics"):

    st.dataframe(
        summary.to_frame("Happiness score")
    )


# Additional information
st.info("Correlation does not imply causation.")

st.caption("Data source: World Happiness Report 2023")