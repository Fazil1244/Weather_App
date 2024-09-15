import streamlit as st
import requests
from datetime import datetime

API_KEY = '1f2477c62e5b33b4cb2b176ebb03dfec'

@st.cache_data
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

def get_background(weather_condition):

    backgrounds = {
        'clear': 'https://wallpapers.com/images/high/sunny-weather-with-cherry-blossom-fr2tn0f21evp0viw.webp',
        'clouds': 'https://wallpapers.com/images/high/cloudy-weather-digital-illustration-hi16vkc00cp99uzv.webp',
        'rain': 'https://wallpapers.com/images/high/rain-desktop-zi3l6ocskkrqmhog.webp',
        'snow': 'https://wallpapers.com/images/high/1080p-winter-background-1920-x-1080-g2t3spl7azx97nsn.webp',
        'thunderstorm': 'https://wallpapers.com/images/high/thunderstorm-blue-ocean-qcuo0fqnxl63hhmy.webp',
        'mist': 'https://wallpapers.com/images/high/weather-background-jlsy4j9gtkqnba9f.webp',
        'default': 'https://wallpapers.com/images/high/tornado-in-stormy-weather-uubp1aloyxznsk7z.webp'
    }

    return backgrounds.get(weather_condition, backgrounds['default'])

def main():
    # Apply a default background when the app first loads
    default_background = get_background('default')
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{default_background}");
            background-size: cover;
            background-position: center;
            color: white;
        }}
        .stMarkdown p, .stTitle, .stTextInput, .stButton button {{
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Weather App")

    city = st.text_input("Enter city name:")

    if st.button("Get Weather"):
        if city:
            with st.spinner('Fetching weather data...'):
                data = get_weather(city)
                if data['cod'] == 200:
                    temp = data['main']['temp']
                    weather = data['weather'][0]['description']
                    humidity = data['main']['humidity']
                    wind_speed = data['wind']['speed']
                    feels_like = data['main']['feels_like']
                    sunrise = datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone']).strftime('%H:%M:%S')
                    sunset = datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone']).strftime('%H:%M:%S')
                    visibility = data.get('visibility', 0) / 1000


                    weather_condition = data['weather'][0]['main'].lower()
                    background_url = get_background(weather_condition)


                    st.markdown(
                        f"""
                        <style>
                        .stApp {{
                            background-image: url("{background_url}");
                            background-size: cover;
                            background-position: center;
                            color: white;
                        }}
                        .stMarkdown p, .stTitle, .stTextInput, .stButton button {{
                            color: #f86f5a;
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True
                    )

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write(f"**Temperature:** {temp}°C")
                        st.write(f"**Feels Like:** {feels_like}°C")
                        st.write(f"**Weather:** {weather.capitalize()}")

                    with col2:
                        st.write(f"**Humidity:** {humidity}%")
                        st.write(f"**Wind Speed:** {wind_speed} m/s")
                        st.write(f"**Visibility:** {visibility} km")

                    with col3:
                        st.write(f"**Sunrise:** {sunrise}")
                        st.write(f"**Sunset:** {sunset}")
                        icon_code = data['weather'][0]['icon']
                        icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
                        st.image(icon_url)
                else:
                    st.error(f"Error: {data['message']}")
        else:
            st.warning("You must enter a city name.")

if __name__ == "__main__":
    main()
