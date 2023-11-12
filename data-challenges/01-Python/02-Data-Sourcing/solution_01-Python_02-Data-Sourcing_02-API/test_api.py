# pylint: disable=missing-docstring,invalid-name

# TODO: paste the code from Kitt's instructions
# $DELETE_BEGIN
import requests

url = "https://www.metaweather.com/api/location/search/?query=london"
response = requests.get(url).json()
city = response[0]
print(f"{city['title']}: {city['woeid']} ({city['latt_long']})")
# $DELETE_END
