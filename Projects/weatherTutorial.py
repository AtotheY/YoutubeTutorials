import urllib
import json

api_endpoint = "http://api.openweathermap.org/data/2.5/weather"

#change this to city = "Toronto" or any specific place if you don't want to input it
city = raw_input()

# Replace with your API KEY
apikey = "xxxReplace With Your Api Keyxxx"

# Put all the components of the URL together
url = api_endpoint + "?q=" + city + "&appid=" + apikey

response = urllib.urlopen(url)
parseResponse = json.loads(response.read())

temperature = parseResponse['main']['temp']
weather = parseResponse['weather'][0]['description']

print temperature
print weather