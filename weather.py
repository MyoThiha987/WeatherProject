from dotenv import load_dotenv
import requests
import os

load_dotenv()


def fetch_weather_conditions(city="Bangkok"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    weather_data = requests.get(url=request_url).json()
    return weather_data


if __name__ == "__main__":
    print("\nFetch current weather conditions *****\n")

    city_name = input("\nEnter a city name :  ")

    if not bool(city_name.strip()):
        city_name = "Bangkok"
    weather_data = fetch_weather_conditions(city=city_name)

    print("\n")
    print(weather_data)
