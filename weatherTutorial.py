import urllib
import json

api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
city = raw_input()
apikey = "b5dec9a7e7e0fdf765f099e3890d5ef2"
url = api_endpoint + "?q=" + city + "&appid=" + apikey

response = urllib.urlopen(url)
parseResponse = json.loads(response.read())

temperature = parseResponse['main']['temp']
weather = parseResponse['weather'][0]['description']

print temperature
print weather