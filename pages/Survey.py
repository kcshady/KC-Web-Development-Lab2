
# This creates the page for users to input data.
# The collected data will be appended to data.csv.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Music Survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("Music Listening Habits Survey")
st.write("Answer the questions below to contribute to our music survey!")

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):

    # Question 1: Favorite genre
    genre_input = st.selectbox(
        "What is your favorite music genre?",
        ["Rock", "Pop", "Hip-Hop/Rap", "Country", "R&B", "Electronic", "Other"]
    )

    # Question 2: Favorite decade
    decade_input = st.selectbox(
        "What is your favorite musical decade?",
        ["1960s", "1970s", "1980s", "1990s", "2000s", "2010s", "2020s"]
    )

    # Question 3: Hours per week
    hours_input = st.number_input(
        "How many hours per week do you listen to music?",
        min_value=0,
        max_value=168,
        value=10,
        step=1
    )

    # Question 4: Streaming service
    service_input = st.selectbox(
        "What is your primary streaming service?",
        ["Spotify", "Apple Music", "YouTube Music", "Amazon Music", "Other"]
    )

    # Question 5: Music and concentration
    concentration_input = st.selectbox(
        "Does music help you concentrate?",
        ["Yes", "No", "Sometimes"]
    )

    # SUBMIT BUTTON
    submitted = st.form_submit_button("Submit Survey")

    if submitted:

        
        new_data = pd.DataFrame([{
            "genre": genre_input,
            "decade": decade_input,
            "hours_per_week": hours_input,
            "streaming_service": service_input,
            "concentration": concentration_input
        }])

        # Add the new row to data.csv
        new_data.to_csv(
            "data.csv",
            mode="a",
            header=False,
            index=False
        )

        st.success("Your survey response has been saved!")

# DATA DISPLAY 
st.divider()
st.header("Current Survey Responses")
# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists("data.csv") and os.path.getsize("data.csv") > 0:
    current_data_df = pd.read_csv("data.csv")
    st.dataframe(current_data_df)
else:
    st.warning("No survey responses have been collected yet.")
