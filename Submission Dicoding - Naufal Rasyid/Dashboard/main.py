# Import necessary libraries
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Download the dataset
# url = "https://drive.google.com/uc?id=1K6mVg-3GP5HWnDykh17sU0sAq3dvCJfp"
df = pd.read_csv ("df_clean.csv")

# Set page configuration
st.set_page_config(
    page_title="Bike Rental Dashboard",
    page_icon="🚲",
    layout="wide",
)

# Main title
st.title('Bike Rental Data Dashboard')

# Sidebar with dataset info
st.sidebar.header('Dataset Info')
st.sidebar.text(f"Number of Rows: {df.shape[0]}")
st.sidebar.text(f"Number of Columns: {df.shape[1]}")

# Display the dataset
st.sidebar.header('Preview Dataset')
st.sidebar.dataframe(df.head())

# Exploratory Data Analysis
st.write("""
## Exploratory Data Analysis

Explore the relationship between windspeed and rental counts.
""")

# Scatter plot of Windspeed vs. Rental Counts
scatter_fig, scatter_ax = plt.subplots(figsize=(10, 6))
scatter_ax.scatter(df['windspeed'], df['cnt'], alpha=0.7, color='skyblue')
scatter_ax.set_xlabel('Windspeed')
scatter_ax.set_ylabel('Rental Count')
scatter_ax.set_title('Relationship between Windspeed and Rental Counts')
st.pyplot(scatter_fig)

# Correlation matrix
st.write("""
## Correlation Matrix

Understand the correlation between different features in the dataset.
""")

correlation_matrix_fig, correlation_matrix_ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=correlation_matrix_ax)
st.pyplot(correlation_matrix_fig)

# Bar plot for Seasonal Rental Counts
st.write("""
## Seasonal Rental Counts

Explore the distribution of rental counts across different seasons.
""")

bar_fig, bar_ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=df, ci=None, palette='viridis', ax=bar_ax)
bar_ax.set_xlabel('Season')
bar_ax.set_ylabel('Rental Count')
bar_ax.set_title('Seasonal Rental Counts')
st.pyplot(bar_fig)
