# weather_utils.py
import requests
from weather_module import Weather


API_KEY = "f87ff710ccb64ce6bce160704250109" 
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def fetch_weather(city):
    """
    Fetches the current weather for a given city from WeatherAPI.com.

    Args:
        city (str): The name of the city.

    Returns:
        Weather: A Weather object with the data, or None if an error occurs.
    """
    # Parameters to be sent with the API request
    params = {
        "key": API_KEY,
        "q": city
    }

    try:
        # Make the GET request to the API
        response = requests.get(BASE_URL, params=params)
        
        # This will raise an exception for HTTP errors (e.g., 401 Unauthorized, 404 Not Found)
        response.raise_for_status() 

        data = response.json()

        # WeatherAPI.com can return a 200 OK status but include an error message in the JSON
        if 'error' in data:
            print(f"Error for city '{city}': {data['error']['message']}")
            return None

        # Extract the relevant information from the JSON response
        weather_obj = Weather(
            city=data['location']['name'],
            temperature=data['current']['temp_c'],
            condition=data['current']['condition']['text'],
            humidity=data['current']['humidity'],
            wind_speed=data['current']['wind_kph'],
            last_updated=data['current']['last_updated']
        )
        return weather_obj

    except requests.exceptions.RequestException as e:
        # Handle network-related errors (e.g., no internet connection)
        print(f"A network error occurred: {e}")
        return None
    except Exception as e:
        # Handle other potential errors (e.g., unexpected JSON structure)
        print(f"An unexpected error occurred: {e}")
        return None