import streamlit as st
from datetime import datetime
import pytz

# Function to get current time in different time zones
def get_time(timezone):
    return datetime.now(pytz.timezone(timezone))

# Function to display clock for a specific time zone
def display_clock(timezone, city):
    current_time = get_time(timezone)
    st.write(f"{city}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

st.title("World Clock")

# Get all time zones
time_zones = pytz.all_timezones

# Get timezone from the user
selected_timezone = st.selectbox("Select Timezone", time_zones)

# Display clock for the selected timezone
display_clock(selected_timezone, selected_timezone)
