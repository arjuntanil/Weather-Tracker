# weather_module.py

class Weather:
    """
    A class to represent the weather information for a specific city.
    """
    
    def __init__(self, city, temperature, condition, humidity, wind_speed, last_updated):
        """Initializes the Weather object with all the necessary attributes."""
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.last_updated = last_updated

    def __str__(self):
        """
        Returns a formatted string representation of the weather details.
        This method is automatically called when you `print()` a Weather object.
        """
        report = (
            f"{self.city}: Temp = {self.temperature}°C, "
            f"Condition = {self.condition}, "
            f"Humidity = {self.humidity}%, "
            f"Wind = {self.wind_speed} km/h, "
            f"Last Updated = {self.last_updated}"
        )
        separator = "-" * (len(report) + 2) # Create a separator line
        return f"{report}\n{separator}"