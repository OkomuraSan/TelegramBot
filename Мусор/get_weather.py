import requests
KEY = "a5264c2c15fe7ddde568e96bfae26847"
def get_lat_and_lon(name = "London"):
    city_name = name
    res = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={KEY}").json()
    return {"lat" : res[0]["lat"], "lon" :res[0]["lon"]}
def get_weather(geoloc):
    lat = geoloc["lat"]
    lon = geoloc["lon"]
    res = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={KEY}]").json()
    return res


geoloc = get_lat_and_lon()
w = get_weather(geoloc)
print(w)

