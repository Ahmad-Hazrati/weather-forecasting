# Required libraries
from time import sleep
from art import *

# Weather Condition Codes
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
THUNDERSTORM = range(200, 300)
DRIZZLE = range(300, 400)
RAIN = range(500, 600)
SNOW = range(600, 700)
ATMOSPHERE = range(700, 800)
CLEAR = range(800, 801)
CLOUDY = range(801, 900)

"""
#Request for user input
#location = input("Enter the city name: ")

#Weather url
# complete_api_link = "https://api.openweathermap.org/data/2.5/forecast?q="
# +location+"&appid="+creds.user_api
# api_link = requests.get(complete_api_link)
# api_data = api_link.json()
"""


def select_weather_display_params(weather_id):
    """
    Selects a weather symbol based on weather condition code
    extracted from the Openweather App.
    """
    if weather_id in THUNDERSTORM:
        display_params = "🌩️"
    elif weather_id in DRIZZLE:
        display_params = "🌧️"
    elif weather_id in RAIN:
        display_params = "🌦️"
    elif weather_id in SNOW:
        display_params = "⛄️"
    elif weather_id in ATMOSPHERE:
        display_params = "💨"
    elif weather_id in CLEAR:
        display_params = "☀️"
    elif weather_id in CLOUDY:
        display_params = "☁️"
    else:
        display_params = "🌈"
    return display_params


def display_forecast_weather_info(api_data, location):
    """
    Prints formatted weather information about a city.
    """
    if api_data["cod"] == "404":
        print("Invalid City: {}, Please check your city name".format(location))
    elif api_data["cod"] == "401":
        print("Invalid API key, Please check your API key")
    else:
        tprint(location.upper())
        dates = []
        for el in api_data["list"]:
            date = el["dt_txt"].split(" ")[0]
            if date in dates:
                continue
            dates.append(date)
            sleep(2)
            temp_city = (el["main"]["temp"] - 273.15)
            feels_like = (el["main"]["feels_like"] - 273.15)
            weather_desc = el["weather"][0]["description"]
            weather_id = el["weather"][0]["id"]
            humidity = el["main"]['humidity']
            wind_spd = el["wind"]["speed"]
            sleep(1)
            print("-----------------------------------------")
            print("Weather Status on - {}  ".format(date))
            print("-----------------------------------------")
            # Assign the the weather_display function
            # to the weather_symbol variable
            weather_symbol = select_weather_display_params(weather_id)
            print("Temperature will be         :" +
                  "{:.2f} deg C".format(temp_city))
            print("It will feel like           :" +
                  "{:.2f} deg C".format(feels_like))
            print("Weather condition will be   :", weather_desc)
            print("Weather description will be :", weather_symbol)
            print("Humidity will be            :", humidity, '%')
            print("And Wind speed will be      :", wind_spd, 'kmph')
            print("---------------------------------------------------------"
                  "-------\n\n")
