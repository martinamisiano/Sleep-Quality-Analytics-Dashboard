import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Sleep Quality Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Sleep Quality Analytics Dashboard")
st.markdown(
    "Interactive analysis of behavioral and physiological sleep factors"
)

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/sleep_data.csv")
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

stress_filter = st.sidebar.slider(
    "Maximum Stress Level",
    int(df["StressLevel"].min()),
    int(df["StressLevel"].max()),
    int(df["StressLevel"].max())
)

caffeine_filter = st.sidebar.slider(
    "Maximum Caffeine Intake",
    int(df["CaffeineIntake"].min()),
    int(df["CaffeineIntake"].max()),
    int(df["CaffeineIntake"].max())
)

filtered_df = df[
    (df["StressLevel"] <= stress_filter)
    &
    (df["CaffeineIntake"] <= caffeine_filter)
]

# KPI Section
st.subheader("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Average Sleep Quality",
        round(filtered_df["SleepQuality"].mean(), 2)
    )

with col2:
    st.metric(
        "Average Sleep Duration",
        round(filtered_df["SleepDuration"].mean(), 2)
    )

with col3:
    st.metric(
        "Average Stress Level",
        round(filtered_df["StressLevel"].mean(), 2)
    )

with col4:
    st.metric(
        "Average Caffeine Intake",
        round(filtered_df["CaffeineIntake"].mean(), 2)
    )

# Correlation Heatmap
st.subheader("Correlation Heatmap")

numeric_df = filtered_df.select_dtypes(include=['number'])

fig1, ax1 = plt.subplots(figsize=(10, 6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="Blues",
    ax=ax1
)

st.pyplot(fig1)

# Scatter Plot
st.subheader("Stress Level vs Sleep Quality")

fig2, ax2 = plt.subplots(figsize=(8, 5))

ax2.scatter(
    filtered_df["StressLevel"],
    filtered_df["SleepQuality"]
)

ax2.set_xlabel("Stress Level")
ax2.set_ylabel("Sleep Quality")

st.pyplot(fig2)

# Distribution Plot
st.subheader("Sleep Quality Distribution")

fig3, ax3 = plt.subplots(figsize=(8, 5))

ax3.hist(filtered_df["SleepQuality"], bins=20)

ax3.set_xlabel("Sleep Quality")
ax3.set_ylabel("Frequency")

st.pyplot(fig3)

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(filtered_df.head(20))

# Footer
st.markdown("---")
st.markdown(
    "Built by Martina Misiano | Healthcare Analytics Project"
)
