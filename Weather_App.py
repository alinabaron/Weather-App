# Weather App
# Using Tkinter displays weather condition and temperature. 
# Using the search bar, enter the city for which you want to see the weather.

import tkinter as tk
import requests
from tkinter import *

API_key = "5606de7a94a03c1dcc00391e7d8a6eb4"

def get_weather(canvas):
    city_name = search_bar.get()
    request_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + API_key
    response = requests.get(request_url).json()
    condition = response['weather'][0]['description']
    temp = round(response['main']['temp'] - 273.15) # converted to Celsius
    feels_like = round(response['main']['feels_like'] - 273.15)
    temp_min = round(response['main']['temp_min'] - 273.15)
    temp_max = round(response['main']['temp_max'] - 273.15)

    output_info = condition + '\n' + str(temp) + '°C'
    info_details = '\n' + 'feels like: ' + str(feels_like) + '°C' + '\n' + 'min: ' + str(temp_min) + '°C' + '\n' + 'max: ' + str(temp_max) + '°C'
    info.config(text=output_info)
    details.config(text=info_details)


canvas = Tk()
canvas.geometry("500x300")
canvas.title('Weather')

fnt = ('Consolas', 28)
small_fnt = ('Consolas', 20)

search_bar = tk.Entry(canvas, font = fnt)
search_bar.pack(pady = 20)
search_bar.focus()
search_bar.bind('<Return>', get_weather)

info = tk.Label(canvas, font=fnt)
info.pack()
details = tk.Label(canvas, font = small_fnt)
details.pack()

canvas.mainloop() 