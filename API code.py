import requests

API_KEY = "YOUR_API_KEY"
CITY = "Bangalore"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    city = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"Weather Report for {city}")
    print("-" * 30)
    print(f"Temperature : {temperature} °C")
    print(f"Humidity    : {humidity}%")
    print(f"Condition   : {weather.title()}")
    print(f"Wind Speed  : {wind_speed} m/s")

except requests.exceptions.RequestException as e:
    print("Error fetching weather data:", e)