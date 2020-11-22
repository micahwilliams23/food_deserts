from bs4 import BeautifulSoup as soup
import requests
import json

radius = '1000000'
# lat = '21.437871'
# lon = '-157.986606'
lat = '44.967243'
lon = '-103.771556'

url = 'https://www.mcdonalds.com/googleapps/GoogleRestaurantLocAction.do?method=searchLocation&latitude=' + lat + '&longitude=' + lon + '&radius=' + radius + '&maxResults=1000000&country=us&language=en-us&webStatusShowClosed=false&showClosed=&hours24Text=Open%2024%20hr'

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'referer': 'https://www.mcdonalds.com/us/en-us/restaurant-locator.html',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

query = {
    'method': 'searchLocation',
    'latitude': lat,
    'longitude': lon,
    'radius': radius,
    'maxResults': '500',
    'county': 'us',
    'language': 'en-us',
    'webStatusShowClosed': 'false',
    'hours24Text': 'Open 24 hr'
}

response = requests.get(url, params = query, headers = req_headers).json()

with open('data/mcds_us.json', 'w') as outfile:
    json.dump(response, outfile)