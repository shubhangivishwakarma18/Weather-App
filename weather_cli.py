import requests
def get_weather(city):
    api_key = "6c9d6b7375f7fa4c917d63750989eeca"  # ← Replace this with your actual key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] != 200:
            print(f"Error: {data['message']}")
        else:
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            print(f"\nWeather in {city.title()}:")
            print(f"🌡 Temperature: {temperature}°C")
            print(f"💧 Humidity: {humidity}%")
            print(f"🌥 Condition: {weather.title()}")

    except Exception as e:
        print("Something went wrong:", e)

# Main
city_input = input("Enter city name: ")
get_weather(city_input)
