import requests, json
from geopy.geocoders import Nominatim
from overwatch import Overwatch
# url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
# geolocator = Nominatim(user_agent="ShitBot")
# location = geolocator.geocode("Garia")
# print(location.address)
# #print(location.raw)
# print((location.latitude, location.longitude))
# lat = location.latitude
# lon = location.longitude
# querystring = {f"lon": lon,"lat": lat}

# headers = {
#     'x-rapidapi-key': "23f2517700msh6142344059b059ep1838a6jsn0f069946c950",
#     'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)
# #print(response.text)
# x = response.json()
# #https://www.weatherbit.io/static/img/icons/{}.png
# #y = x["data"]
# #app_temp = y["app_temp"]
# #t = y["temp"]
# #st = y["st"]
# #print(st)
overwatch = Overwatch(battletag="NyxBoi#1487")
print(overwatch())