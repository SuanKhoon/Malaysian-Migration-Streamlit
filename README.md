# 🌏 Malaysia Migration Insights Dashboard

**Analyze foreign entries into Malaysia by various dimensions.**

This Streamlit dashboard enables users to explore and analyze foreign migration data into Malaysia based on different criteria like year, month, gender, and state. The dashboard provides various visualizations, including bar charts, line graphs, and pie charts, to give insights into foreign entries by country, gender, and state.

## Features

- **Year and Month Selection:** Users can filter the data by selecting specific years and months.
- **Gender Selection:** Filter the data to view foreign entries by either male or female arrivals.
- **State Selection:** View migration data specific to the states of Malaysia.
- **Data Visualizations:**
  - Total foreign entries by gender and year.
  - Percentage change in foreign entries over the years.
  - Foreign entry distribution by state (Pie Chart).
  - Top 5 foreign entry countries.
  - Total foreign entries to each state.

## Visualizations Included

1. **Total Foreign Entries by Gender and Year:** A bar chart showing the total entries based on the selected gender and years.
2. **Percentage Change of Foreign Entries:** A line chart depicting the percentage increase or decrease of foreign entries year-on-year for the selected gender.
3. **Foreign Entry Distribution by State:** A pie chart visualizing the percentage of foreign entries into each Malaysian state.
4. **Top 5 Countries by Foreign Entries:** A bar chart displaying the top 5 countries with the highest foreign entries.
5. **Total Foreign Entries to Each State:** A bar chart showing total entries by state.

## Purpose

This dashboard aims to provide insights into the total number of foreign entries into Malaysia and its various states, enabling stakeholders to analyze trends based on gender, country of origin, and other filters.

## Installation

**Clone this repository:**
   ```bash
   git clone https://github.com/SuanKhoon/Malaysian-Migration-Streamlit.git
   cd MalaysiaMigrationInsights

To run this dashboard locally, follow the steps below:

1. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Place the data file (`arrivals_soe.csv`) in the root directory.**

4. **Run the Streamlit app:**
   ```bash
   streamlit run main.py
   ```

5. Open your browser and go to `http://localhost:8501` to view the dashboard.

## Dependencies

- **Streamlit**: For building the interactive web app.
- **Pandas**: For data processing and manipulation.
- **Plotly Express**: For creating interactive charts and visualizations.

Install all dependencies using the command:  
```bash
pip install -r requirements.txt
```

## Folder Structure

```
MalaysiaMigrationInsights/
│
├── arrivals_soe.csv            # The data file to be analyzed
├── main.py                     # Main Streamlit application
├── requirements.txt            # Python dependencies
└── README.md                   # Documentation
```

## Data

The data used in this dashboard is sourced from the `arrivals_soe.csv` file, containing information on foreign entries into Malaysia. Key columns include:

- `Date`: The date of the foreign entry.
- `Country`: The country of origin.
- `Migration State`: The state in Malaysia where the entry occurred.
- `Arrivals`: Total number of foreign entries.
- `Arrivals: Gender Male`: Number of male arrivals.
- `Arrivals: Gender Female`: Number of female arrivals.
