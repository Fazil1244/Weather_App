🌤 Streamlit Weather App
python project

The provided Python script is a Streamlit application designed to fetch and display weather information for a specified city. Here’s a detailed description of how the program works:

Overview

#Libraries Used:

streamlit for building the web application interface.

requests for making HTTP requests to the OpenWeatherMap API.

datetime for handling and formatting dates and times.

API Key: The script uses an API key (API_KEY = '1f2477c62e5b33b4cb2b176ebb03dfec') to access weather data from OpenWeatherMap.

Functionality Caching Weather Data:

The function get_weather(city) is decorated with @st.cache_data to cache the weather data for efficiency. This avoids making repeated API calls for the same city, thus speeding up the app.

Styling the App:

The st.markdown function is used to apply custom CSS styling to the app. It sets a background image and changes text colors to white for better visibility against the background.

User Interface:

Title: The app’s title is set to "Weather App".

City Input: A text input field allows users to enter the name of the city they want to get weather information for.

Button: A button labeled "Get Weather" triggers the process of fetching weather data when clicked.

Fetching and Displaying Weather Data:

When the user clicks "Get Weather", the app fetches weather data using the OpenWeatherMap API.

The response is processed, and various weather details are displayed:

Temperature: Current temperature in Celsius.

Feels Like: Temperature that it "feels like".

Weather Description: General description of the weather.

Humidity: Percentage of humidity.

Wind Speed: Speed of the wind in meters per second.

Visibility: Visibility distance in kilometers.

Sunrise and Sunset Times: Times of sunrise and sunset formatted in HH:MM:SS.

Weather Icon: An image representing the current weather condition.

Error Handling:

If there’s an issue with the API request (e.g., city not found), an error message is displayed to the user.

If the user doesn’t enter a city name, a warning message is shown.

How It Works Initial Setup:

The main() function is executed when the script is run. It initializes the app’s layout and style.

User Interaction:

Users input the city name and click the "Get Weather" button. The get_weather function makes an API request to OpenWeatherMap, retrieves the data, and returns it in JSON format. Data Presentation:

The app processes the JSON response and displays relevant weather information in three columns for a structured view. Weather conditions are visualized with an icon from the OpenWeatherMap API. Key Points Styling: Custom CSS is used to enhance the visual appearance of the app. API Interaction: The app communicates with an external API to fetch real-time weather data. User Experience: The app provides feedback (loading spinner, error messages) to improve the user experience. This script provides a straightforward and interactive way to get current weather information using Streamlit, with an emphasis on visual appeal and user feedback.
