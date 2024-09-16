import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="Malaysia Foreign Entries Dashboard",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add a title and a subheader
st.title("🌏 Malaysia Foreign Entries Dashboard")
st.subheader("Analyze foreign entries into Malaysia by various dimensions")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('arrivals_soe.csv')
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month_name()
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Data Here:")

# Year selection
years = df['Year'].sort_values().unique()
selected_years = st.sidebar.multiselect(
    "Select Year(s):", options=years, default=years)

# Month selection
months = df['Month'].unique()
selected_months = st.sidebar.multiselect(
    "Select Month(s):", options=months, default=months)

# Gender selection
genders = ['Male', 'Female']
selected_gender = st.sidebar.selectbox("Select Gender:", options=genders)

# State selection
states = df['Migration State'].unique()
selected_states = st.sidebar.multiselect(
    "Select State(s):", options=states, default=states)

# Filter data based on selections
filtered_df = df[
    (df['Year'].isin(selected_years)) &
    (df['Month'].isin(selected_months)) &
    (df['Migration State'].isin(selected_states))
]

# Gender-specific arrivals column
gender_column = 'Arrivals: Gender Male' if selected_gender == 'Male' else 'Arrivals: Gender Female'

# 1) Total amount foreign entry by Gender (x-axis) by Year (y-axis)
st.markdown("### Total Foreign Entries by Gender and Year")
total_entries = filtered_df.groupby('Year')[gender_column].sum().reset_index()
fig1 = px.bar(total_entries, x='Year', y=gender_column,
              color_discrete_sequence=['#1f77b4'])
st.plotly_chart(fig1, use_container_width=True)

# 2) Percentage increase/decrease of foreign entries by Gender and Year
st.markdown("### Percentage Change of Foreign Entries by Gender and Year")
total_entries['Percentage Change'] = total_entries[gender_column].pct_change() * 100
fig2 = px.line(total_entries, x='Year', y='Percentage Change', markers=True)
st.plotly_chart(fig2, use_container_width=True)

# 3) Total Foreign Nationals by Year (including males and females)
st.markdown("### Total Foreign Nationals Entering Malaysia by Year")
total_nationals = filtered_df.groupby('Year').agg(
    Total_Arrivals=pd.NamedAgg(column='Arrivals', aggfunc='sum')
).reset_index()
fig3 = px.bar(total_nationals, x='Year', y='Total_Arrivals',
              color_discrete_sequence=['#ff7f0e'])
st.plotly_chart(fig3, use_container_width=True)
