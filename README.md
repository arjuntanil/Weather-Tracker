# Weather Tracker 🌦️

A command-line Python application that fetches and displays real-time weather data for multiple cities using the [WeatherAPI.com](https://www.weatherapi.com/) service. This project demonstrates modular programming, object-oriented principles, and external API integration.

---

## ✨ Core Features

* **Real-Time Data:** Fetches current weather information from a live API.
* **Multi-City Support:** Allows users to input and get reports for multiple cities in one go.
* **Object-Oriented:** Uses a `Weather` class to neatly structure and handle the data for each city.
* **Modular Design:** Code is separated into modules for API utilities (`weather_utils.py`), the data class (`weather_module.py`), and the main application logic (`main.py`).
* **Robust Error Handling:** Gracefully handles invalid city names and network connectivity issues.

---

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Get a Free API Key
This project requires a key from WeatherAPI.com.
* Go to **[WeatherAPI.com](https://www.weatherapi.com/)** and sign up for a free account.
* Log in to your dashboard and copy your **API Key**.



**Clone the repository:**
    ```bash
    git clone [https://github.com/arjuntanil/Weather-Tracker.git](https://github.com/arjuntanil/Weather-Tracker.git)
    ```
### Create the virtual environment
python -m venv venv

### Activate on Windows
.\venv\Scripts\activate

### Activate on macOS/Linux
source venv/bin/activate

**Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### in weather_utils.py
API_KEY = "f87ff710ccb64ce6bce160704250109"

### This terminal will run the main script that fetches data, applies bonuses, and sends updates back to the server.


```bash
python main.py
```


### Output 

Enter city names (type 'done' to finish):
City: Thrissur
City: London
City: Tokyo
City: fakecity
City: done

Weather Report:
Error for city 'fakecity': No matching location found.
Thrissur: Temp = 27.0°C, Condition = Mist, Humidity = 94%, Wind = 3.6 km/h, Last Updated = 2025-09-01 21:45
----------------------------------------------------------------------------------------------------------
London: Temp = 18.0°C, Condition = Overcast, Humidity = 82%, Wind = 20.5 km/h, Last Updated = 2025-09-01 17:15
-----------------------------------------------------------------------------------------------------------------
Tokyo: Temp = 26.0°C, Condition = Sunny, Humidity = 65%, Wind = 15.1 km/h, Last Updated = 2025-09-02 05:45
-----------------------------------------------------------------------------------------------------------






### 🛠️ Application Flow

The program follows a simple, logical flow:

* User Input: The main.py script starts by creating a loop that collects city names from the user until they type done.

* API Call: For each city entered, main.py calls the fetch_weather() function located in weather_utils.py.

* Data Fetching: The fetch_weather() function builds and sends a GET request to the WeatherAPI.com server. It includes the city name and your secret API key.

* Object Creation: If the API returns valid data, fetch_weather() uses the Weather class from weather_module.py to create a Weather object, neatly organizing the city's temperature, humidity, etc.

* Error Handling: If the API returns an error (e.g., for an invalid city) or if a network problem occurs, fetch_weather() prints an error message and returns None.

* Display Report: main.py receives the Weather object (or None). If the object is valid, it simply prints it. This automatically calls the object's __str__ method, which formats the weather details into a clean, readable report for the user.






