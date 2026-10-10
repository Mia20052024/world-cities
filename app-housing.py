import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("housing.csv")

st.title("California Housing Data (1990) by Mia")

minimum_value = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000
)

filtered_df = df[df["median_house_value"] >= minimum_value]

st.subheader("See more filters in the sidebar:")

location_types = sorted(df["ocean_proximity"].dropna().unique())

selected_locations = st.sidebar.multiselect(
    "Choose the location type",
    options=location_types,
    default=location_types
)

filtered_df = filtered_df[
    filtered_df["ocean_proximity"].isin(selected_locations)
]

income_level = st.sidebar.radio(
    "Choose income level",
    ["Low", "Medium", "High"]
)

if income_level == "Low":
    filtered_df = filtered_df[filtered_df["median_income"] <= 2.5]
elif income_level == "Medium":
    filtered_df = filtered_df[
        (filtered_df["median_income"] > 2.5)
        & (filtered_df["median_income"] < 4.5)
    ]
else:
    filtered_df = filtered_df[filtered_df["median_income"] >= 4.5]

st.map(filtered_df[["latitude", "longitude"]])

st.subheader("Median House Value Distribution")

fig, ax = plt.subplots()
ax.hist(filtered_df["median_house_value"], bins=30)
ax.set_xlabel("Median House Value (USD)")
ax.set_ylabel("Number of Districts")

st.pyplot(fig)