from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# Available factors
FACTORS = {
    "GDP per capita (log)": "log_gdp",
    "Social support": "social_support",
    "Healthy life expectancy": "life_expectancy",
    "Freedom": "freedom",
    "Generosity": "generosity",
    "Perceptions of corruption": "corruption"
}


# Load and prepare the dataset
def load_data():

    data_path = (
        Path(__file__).parent
        / "data"
        / "happiness_data_2023.csv"
    )

    df = pd.read_csv(data_path)

    df = df.rename(columns={
        "Country name": "country",
        "Ladder score": "happiness",
        "Logged GDP per capita": "log_gdp",
        "Social support": "social_support",
        "Healthy life expectancy": "life_expectancy",
        "Freedom to make life choices": "freedom",
        "Generosity": "generosity",
        "Perceptions of corruption": "corruption"
    })

    columns = ["country", "happiness"] + list(FACTORS.values())

    return df[columns]


# Filter the dataset by country
def get_country_data(df, country):

    return df[df["country"] == country]


# Calculate descriptive statistics
def calculate_summary(df):

    return df["happiness"].describe()


# Calculate Pearson correlation
def calculate_correlation(df, factor_column):

    return df[factor_column].corr(df["happiness"])


# Calculate correlations for all factors
def calculate_all_correlations(df):

    correlations = {}

    for name, column in FACTORS.items():

        correlations[name] = calculate_correlation(df, column)

    return pd.Series(correlations).sort_values(ascending=False)


# Create a scatter plot
def create_scatter_plot(df, country, factor):

    factor_column = FACTORS[factor]

    selected_country = get_country_data(df, country)

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.scatter(
        df[factor_column],
        df["happiness"],
        color="steelblue",
        alpha=0.5,
        label="Countries"
    )

    ax.scatter(
        selected_country[factor_column],
        selected_country["happiness"],
        color="darkorange",
        s=120,
        label=country
    )

    ax.set_xlabel(factor)
    ax.set_ylabel("Happiness score")
    ax.set_title(f"{factor} vs. Happiness")

    ax.grid(alpha=0.2)
    ax.legend()

    fig.tight_layout()

    return fig