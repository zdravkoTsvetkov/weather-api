import os
from dotenv import load_dotenv
import requests

load_dotenv()


def fetch_current_weather(api_key, location):
    base_url = 'https://api.weatherapi.com/v1/current.json'
    params = {
        'key': api_key,
        'q': location,
        'aqi': 'yes'
    }

    try:
        response = requests.get(base_url, params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')


def display_weather(data: dict):
    location = data['location']['name']
    region = data['location']['region']
    country = data['location']['country']
    temp_c = data['current']['temp_c']
    condition = data['current']['condition']['text']
    humidity = data['current']['humidity']

    print(f'Current weather in {location}, {region}, {country}: ')
    print(f'Temperature: {temp_c}')
    print(f'Condition: {condition}')
    print(f'Humidity: {humidity}')


def save_weather_data(data: dict, filename):
    with open(filename, 'w') as f:
        f.write('Weather data:\n')
        f.write(
            f"Location: {data['location']['name']}, {data['location']['region']}, {data['location']['country']}\n"
        )
        f.write(f"Temperatute: {data['current']['temp_c']}\n")
        f.write(f"Condition: {data['current']['condition']['text']}\n")
        f.write(f"Humidity: {data['current']['humidity']}\n")

    print(f"Weather data saved to {filename}")


def main():
    api_key = os.environ.get('API_KEY')
    weather_data = fetch_current_weather(api_key, 'Plovdiv')
    display_weather(weather_data)
    save_weather_data(weather_data, './weather_data.txt')


main()
