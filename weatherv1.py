import requests
import streamlit as st

api = "7f54d7b69c1c881eb524c686b05c6157"

st.title("The Weather In ___")


city = st.text_input("Enter City Here:", key="city_input")

if city:
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api}"
    )

    if weather_data.status_code == 200:
        st.write("Getting Data...")
        weather_json = weather_data.json()
        weather = weather_json['weather'][0]['main']
        temp = weather_json['main']['temp']


        st.title(f"Weather: {weather}")
        st.title(f"Temp: {temp}°F")
    else:
        st.write("Failed, try again.")
