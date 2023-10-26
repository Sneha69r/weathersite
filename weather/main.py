# to fetch data from a web API
import requests
import json # string to dict
import pyttsx3 #text-to-speech functionality.
text_to_speech = pyttsx3.init()
city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=68cf1a82d61946afa2b141401232510&q={city}"

r = requests.get(url)
# print(r.text)

wdic = json.loads(r.text)
temp = wdic["current"]["temp_c"]
humi = wdic["current"]["humidity"]
feels = wdic["current"]["feelslike_c"]
text_to_speech.say(f"the current weather in {city} is {temp} degree and humidity is {humi} and its feelslike {feels}")
text_to_speech.runAndWait()

print(f"the current weather in {city} is {temp} degree and humidity is {humi} and its feelslike {feels}")