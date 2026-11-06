# This creates the page for displaying data visualizations.

import json
import pandas as pd
import plotly.express as px
import streamlit as st

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈")


# PART 1: GRAPHS FROM data.json
with open("data.json") as f:
    data = json.load(f)

df = pd.DataFrame(data["data_points"])
st.header(data["chart_title"])

# Static chart: bar chart (advanced element, Plotly)
fig1 = px.bar(
    df,
    x="title",
    y="my_rating",
    color="artist",
    title="My Rating by Song",
    labels={"title": "Song", "my_rating": "My Rating (1-10)"}
)
st.plotly_chart(fig1)

# Dynamic chart: scatter plot with a radio button and session state
if "y_choice" not in st.session_state:
    st.session_state.y_choice = "length_min"

st.radio(
    "Choose what to plot against year:",
    ["length_min", "my_rating"],
    key="y_choice"
)


fig2 = px.scatter(
    df,
    x="year",
    y=st.session_state.y_choice,
    hover_data=["title", "artist", "album"],
    title=f"{st.session_state.y_choice} by Release Year",
    labels={
        "year": "Release Year",
        "length_min": "Song Length (minutes)",
        "my_rating": "My Rating (1-10)"
    }
)
st.plotly_chart(fig2)

# PART 2: GRAPHS FROM data.csv
# --- YOUR CODE GOES HERE ---

# PART 2: GRAPHS FROM data.csv

# Read the survey responses from the CSV file
import os

if os.path.exists("data.csv") and os.path.getsize("data.csv") > 0:

    survey_df = pd.read_csv("data.csv")

    st.header("Music Survey Results")

    st.subheader("Favorite Music Genres")

    genre_counts = survey_df["genre"].value_counts().reset_index()
    genre_counts.columns = ["Genre", "Number of Responses"]

    fig3 = px.bar(
        genre_counts,
        x="Genre",
        y="Number of Responses",
        title="Most Popular Music Genres",
        labels={
            "Genre": "Music Genre",
            "Number of Responses": "Number of People"
        }
    )

    st.plotly_chart(fig3)


    st.subheader("Explore Other Survey Results")

    if "chart_choice" not in st.session_state:
        st.session_state.chart_choice = "decade"

    st.radio(
        "Choose which survey results to view:",
        ["decade", "streaming_service", "concentration"],
        key="chart_choice"
    )

    selected_counts = (
        survey_df[st.session_state.chart_choice]
        .value_counts()
        .reset_index()
    )

    selected_counts.columns = ["Response", "Number of People"]

    fig4 = px.pie(
        selected_counts,
        names="Response",
        values="Number of People",
        title=f"Survey Results: {st.session_state.chart_choice.replace('_', ' ').title()}"
    )

    st.plotly_chart(fig4)

else:
    st.info("Complete the survey to see the results here.")
