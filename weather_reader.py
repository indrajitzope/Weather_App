import requests

def get_weather(city_name, api_key):
    """
    Fetch weather data for a given city using OpenWeatherMap API.
    
    :param city_name: Name of the city.
    :param api_key: Your OpenWeatherMap API key.
    :return: Weather data as a dictionary or an error message.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()

        # Extract relevant information
        weather = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']} °C",
            "Weather": data["weather"][0]["description"].capitalize(),
            "Humidity": f"{data['main']['humidity']}%",
            "Wind Speed": f"{data['wind']['speed']} m/s"
        }
        return weather
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

if __name__ == "__main__":
    # Replace with your OpenWeatherMap API key
    API_KEY = "your_openweathermap_api_key"

    # Ask for city name
    city = input("Enter city name: ")
    weather_info = get_weather(city, API_KEY)

    # Print weather information
    if "Error" in weather_info:
        print(f"Error: {weather_info['Error']}")
    else:
        print("Weather Information:")
        for key, value in weather_info.items():
            print(f"{key}: {value}")
