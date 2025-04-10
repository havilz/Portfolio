
import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Disaster Dashboard Asia", layout="wide")

@st.cache_data
def load_data():
    data = pd.read_csv("data_cleaned_renamed.csv")
    return data

data = load_data()


with st.sidebar:
    st.header("Filter")
    country = st.multiselect("Select Country", options=data["Country"].unique(), default=data["Country"].unique())
    year = st.slider("Select Year Range", int(data["Start Year"].min()), int(data["Start Year"].max()), (2010, 2025))
    disaster_type = st.multiselect("Disaster Type", options=data["Disaster Type"].unique(), default=data["Disaster Type"].unique())

filtered = data[
    (data["Country"].isin(country)) &
    (data["Start Year"] >= year[0]) & (data["Start Year"] <= year[1]) &
    (data["Disaster Type"].isin(disaster_type))
]

st.subheader("General Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Disasters", len(filtered))
col2.metric("Total Deaths", int(filtered["Total Deaths"].sum()))
col3.metric("Total Damage (US$)", f"{int(filtered['Total Damage'].sum() * 1000):,}")

st.subheader("Disaster Count by Type")
disaster_count = filtered["Disaster Type"].value_counts().reset_index()
disaster_count.columns = ["Disaster Type", "Count"]
st.plotly_chart(px.bar(disaster_count, x="Disaster Type", y="Count", title="Disasters by Type"))

st.subheader("Social Impact")
social_cols = ["Total Deaths", "No. Injured", "No. Affected", "No. Homeless"]
social_data = filtered[social_cols].sum().reset_index()
social_data.columns = ["Impact", "Total"]
st.plotly_chart(px.bar(social_data, x="Impact", y="Total", title="Total Social Impact"))

st.subheader("Economic Impact")
econ_cols = ["Total Damage", "Aid Contribution", "Reconstruction Costs"]
econ_data = filtered[econ_cols].sum().reset_index()
econ_data.columns = ["Economic Metric", "Total"]
econ_data["Total"] = econ_data["Total"] * 1000
st.plotly_chart(px.bar(econ_data, x="Economic Metric", y="Total", title="Total Economic Impact (in US$)"))

st.subheader("Disaster Trend Over Time")
trend = filtered.groupby("Start Year").size().reset_index(name="Count")
st.plotly_chart(px.line(trend, x="Start Year", y="Count", title="Disasters Over Years"))

st.subheader("Disaster Locations Map")
filtered = filtered.dropna(subset=["Latitude", "Longitude"])
m = folium.Map(location=[25, 100], zoom_start=4)
for _, row in filtered.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=5,
        popup=f"{row['Disaster Type']} ({row['Start Year']})",
        color="crimson",
        fill=True,
        fill_color="crimson"
    ).add_to(m)
st_data = st_folium(m, width=1200, height=500)

st.markdown("---")
st.caption("Data source: Cleaned EM-DAT-like Dataset")
