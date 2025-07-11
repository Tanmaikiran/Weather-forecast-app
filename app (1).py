import streamlit as st
import requests

st.set_page_config(page_title="Weather App", page_icon="🌤️")
st.title("🌤️ Weather Forecast App")

city = st.text_input("Enter city name:")

if city:
    api_key = "2805c5e870303f6f4c409e1f71bfe426"  # Your working API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        st.subheader(f"Weather in {city}")
        st.write(f"🌡️ Temperature: {data['main']['temp']} °C")
        st.write(f"🤒 Feels Like: {data['main']['feels_like']} °C")
        st.write(f"☁️ Weather: {data['weather'][0]['description'].title()}")
        st.write(f"💨 Wind Speed: {data['wind']['speed']} m/s")
        st.write(f"💧 Humidity: {data['main']['humidity']}%")
    else:
        st.error("City not found or API error.")
