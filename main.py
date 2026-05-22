import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title
st.title("Student Performance Dashboard")
st.write("This is the sample dashboard")

# Data
data = {
    "T1": [66, 89, 78, 92],
    "T2": [91, 68, 68, 82],
    "T3": [76, 99, 68, 72],
}

# Create DataFrame
df = pd.DataFrame(data, index=["s1", "s2", "s3", "s4"])

# Display table
st.subheader("Marks Card")
st.dataframe(df)

# Line chart
st.subheader("Performance")
st.line_chart(df.T)