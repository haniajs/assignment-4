import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # For Celsius, use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temp = main['temp']
        humidity = main['humidity']
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_desc}")
    else:
        print(f"Error fetching weather data for {city}. Please check the city name or your API key.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
    get_weather(city, api_key)
