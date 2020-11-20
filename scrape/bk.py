from bs4 import BeautifulSoup as soup
import requests
import json

minLat = '-89.999'
minLon = '-179.999'
maxLat = '89.999'
maxLon = '179.999'
userLat = '0'
userLon = '0'

url = 'https://czqk28jt.apicdn.sanity.io/v1/data/query/prod_bk_us?query=*%5B%20_type%20%3D%3D%20%27restaurant%27%20%26%26%20environment%20%3D%3D%20%24environment%20%26%26%20!(%24appEnvironemnt%20in%20coalesce(hideInEnvironments%2C%20%5B%5D))%20%26%26%20latitude%20%3E%20%24minLat%20%26%26%20latitude%20%3C%20%24maxLat%20%26%26%20longitude%20%3E%20%24minLng%20%26%26%20longitude%20%3C%20%24maxLng%20%26%26%20status%20%3D%3D%20%24status%20%5D%20%7Corder((%24userLat%20-%20latitude)%20**%202%20%2B%20(%24userLng%20-%20longitude)%20**%202)%5B%24offset...(%24offset%20%2B%20%24limit)%5D%20%7Blatitude%2Clongitude%2CphysicalAddress%2CrestaurantImage%7B...%2C%20asset-%3E%7D%7D&%24appEnvironemnt=%22prod%22&%24environment=%22prod%22&%24limit=100000&%24maxLat='+maxLat+'&%24maxLng='+maxLon+'&%24minLat='+minLat+'&%24minLng='+minLon+'&%24offset=0&%24status=%22Open%22&%24userLat='+userLat+'&%24userLng='+userLon

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

query = {
    "query": "*[ _type == 'restaurant' && environment == $environment && !($appEnvironemnt in coalesce(hideInEnvironments, [])) && latitude > $minLat && latitude < $maxLat && longitude > $minLng && longitude < $maxLng && status == $status ] |order(($userLat - latitude) ** 2 + ($userLng - longitude) ** 2)[$offset...($offset + $limit)] {latitude,longitude,name,physicalAddress}"
}

response = requests.get(url, headers = req_headers).json()

with open('data/bk_us.json', 'w') as outfile:
    json.dump(response, outfile)