
import streamlit as st
import requests

st.set_page_config(page_title="Weather App", page_icon="🌤️")
st.title("🌤️ Weather Forecast App")

city = st.text_input("Enter city name:")

if city:
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        st.subheader(f"Weather in {city}")
        st.write(f"🌡️ Temperature: {data['main']['temp']} °C")
        st.write(f"☁️ Weather: {data['weather'][0]['description'].title()}")
        st.write(f"💨 Wind Speed: {data['wind']['speed']} m/s")
    else:
        st.error("City not found or API error.")
