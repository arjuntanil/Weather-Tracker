# main.py
from weather_utils import fetch_weather

def main():
    """
    Main function to run the Weather Tracker application.
    """
    cities = []
    print("Enter city names (type 'done' to finish):")

    # 1. Collect city names from the user
    while True:
        city_input = input("City: ").strip()
        if city_input.lower() == 'done':
            break
        if city_input: # Ensure the input is not empty
            cities.append(city_input)

    if not cities:
        print("\nNo cities entered. Exiting.")
        return

    # 2. Fetch and display the weather report for each city
    print("\nWeather Report:")
    weather_reports = []

    for city in cities:
        # The fetch_weather function handles API calls and error checking
        weather_data = fetch_weather(city)
        if weather_data:
            # If successful, add the Weather object to our list
            weather_reports.append(weather_data)
    
    # 3. Print all the successfully fetched reports
    for report in weather_reports:
        # The __str__ method in the Weather class is automatically called here
        print(report)

if __name__ == '__main__':
    main()