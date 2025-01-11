import requests 
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"

def get_weather(city):
    params = {
        'key': os.getenv('WEATHER_API_KEY'),
        'q': city
    }
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    print('------------------------------------------------------------')
    print('------------------------------------------------------------')
    print('------------------------------------------------------------')
    print("***************Weather App**********************************")
    print("This app will provide you with the current weather information for a given city.")
    print('------------------------------------------------------------')
    print("Please note that the weather data is provided by WeatherAPI.com")
    print("Hello, welcome to the weather app")
    print("Example: Miami F")
    
    while True:
        user_input = input("Please enter the city name and C for Celsius or F for Fahrenheit, or q to quit: ").strip()
        if user_input.lower() == "q":
            break
        
        parts = user_input.split()
        if len(parts) != 2:
            print("Invalid input. Please enter the city name followed by C or F for temperature unit.")
            continue
        
        city, unit = parts
        unit = unit.upper()
        
        weather = get_weather(city)
        if weather:
            if unit == "C":
                temp = weather['current']['temp_c']
                print(f"The temperature in {city} is {temp} degrees Celsius, and the current condition is {weather['current']['condition']['text']}")
            elif unit == "F":
                temp = weather['current']['temp_f']
                print(f"The temperature in {city} is {temp} degrees Fahrenheit, and the current condition is {weather['current']['condition']['text']}")
            else:
                print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
        else:
            print(f"Error fetching data for {city}. Please check the city name and try again.")

if __name__ == "__main__":
    main()
