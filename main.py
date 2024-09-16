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

# 4) Total Foreign Nationals by Year (Male + Female)
st.markdown("### Total Foreign Nationals Entering Malaysia (Male + Female) by Year")
total_nationals_gender = filtered_df.groupby('Year').agg(
    Total_Arrivals_Male=pd.NamedAgg(column='Arrivals: Gender Male', aggfunc='sum'),
    Total_Arrivals_Female=pd.NamedAgg(column='Arrivals: Gender Female', aggfunc='sum')
).reset_index()
total_nationals_gender['Total_Arrivals'] = total_nationals_gender['Total_Arrivals_Male'] + total_nationals_gender['Total_Arrivals_Female']
fig4 = px.bar(total_nationals_gender, x='Year', y='Total_Arrivals',
              color_discrete_sequence=['#2ca02c'])
st.plotly_chart(fig4, use_container_width=True)

# 5) Percentage increase/decrease of foreign entries by State (Pie Chart)
st.markdown("### Percentage of Foreign Entries by State")
state_entries = filtered_df.groupby('Migration State')['Arrivals'].sum().reset_index()

# Create pie chart and adjust layout to add padding
fig5 = px.pie(state_entries, names='Migration State', values='Arrivals')

# Add padding at the bottom to ensure labels are visible
fig5.update_layout(
    margin=dict(t=1, b=120, l=1, r=1)  # Adjust the bottom (b) padding as needed
)

st.plotly_chart(fig5, use_container_width=True)

# 6) Top 5 foreign entries by Country
st.markdown("### Top 5 Countries by Foreign Entries")
country_entries = filtered_df.groupby('Country')['Arrivals'].sum().reset_index()
top_countries = country_entries.nlargest(5, 'Arrivals')
fig6 = px.bar(top_countries, x='Country', y='Arrivals', color='Country')
st.plotly_chart(fig6, use_container_width=True)

# 7) Total Foreign Entry to Each State
st.markdown("### Total Foreign Entries to Each State")
state_total_entries = filtered_df.groupby('Migration State')['Arrivals'].sum().reset_index()
fig7 = px.bar(state_total_entries, x='Migration State',
              y='Arrivals', color='Arrivals')
st.plotly_chart(fig7, use_container_width=True)

# Footer
st.markdown("---")
