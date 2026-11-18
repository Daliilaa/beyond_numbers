# Beyond Numbers 🌍

**Exploring the Factors Behind Global Happiness**

Beyond Numbers is an interactive data science dashboard exploring how economic and social factors are associated with life satisfaction across countries. It combines statistical analysis in Python with a Streamlit web interface.

## Features

- Interactive country and factor selection
- Country happiness score compared with the average across countries
- Pearson correlation analysis for six socioeconomic factors
- Dynamic scatter plots highlighting the selected country
- Bar chart comparing all six correlation coefficients
- Descriptive statistics, including mean, median, standard deviation and quartiles
<img width="792" height="587" alt="image" src="https://github.com/user-attachments/assets/f1dff8dd-2628-409b-8881-87c1f4abadeb" />

## Technologies

- Python — application logic
- Pandas — data preparation and statistical analysis
- Matplotlib — data visualization
- Streamlit — interactive web interface

## Project structure

```text
beyond-numbers/
├── data/
│   └── happiness_data_2023.csv  # supplied locally
├── analysis.py                 # Data preparation and analysis functions
├── app.py                      # Streamlit user interface
├── requirements.txt            # Python dependencies
├── .gitignore
└── README.md
```

The project separates statistical logic from the user interface (Separation of Concerns). The analysis module provides reusable functions, while the application module handles user input, calls those functions and displays the results.

## Getting started

### 1. Create a virtual environment

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install pandas matplotlib streamlit
```

If a `requirements.txt` file is available, you can instead run:

```bash
python -m pip install -r requirements.txt
```

### 3. Prepare the dataset

Create a `data/` directory in the project root and place the World Happiness Report 2023 CSV file inside it, named `happiness_data_2023.csv`.

The expected columns are `Country name`, `Ladder score`, `Logged GDP per capita`, `Social support`, `Healthy life expectancy`, `Freedom to make life choices`, `Generosity`, and `Perceptions of corruption`.

The CSV is excluded from version control until its redistribution permissions are confirmed.

### 4. Run the application

```bash
python -m streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser if it does not open automatically.

## Statistical methodology

The dashboard calculates Pearson correlation coefficients between the happiness score and each of the six factors, using all available complete pairs of observations. Selecting a country highlights its position in the scatter plot; it does not restrict the correlation calculation to that country.

The country average is unweighted by population. Correlations measure linear association and do not imply causation. This project is an exploratory analysis of country-level data, not a causal or predictive model.

## Data source

World Happiness Report 2023 — https://worldhappiness.report/ed/2023/

The exact CSV download source and redistribution terms should be documented before publishing the dataset.
