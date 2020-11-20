from bs4 import BeautifulSoup as soup
import requests
import json

minLat = '-89.999'
minLon = '-179.999'
maxLat = '89.999'
maxLon = '179.999'
userLat = '0'
userLon = '0'

# url = 'https://czqk28jt.apicdn.sanity.io/v1/data/query/prod_bk_us?query=*%5B%20_type%20%3D%3D%20%27restaurant%27%20%26%26%20environment%20%3D%3D%20%24environment%20%26%26%20!(%24appEnvironemnt%20in%20coalesce(hideInEnvironments%2C%20%5B%5D))%20%26%26%20latitude%20%3E%20%24minLat%20%26%26%20latitude%20%3C%20%24maxLat%20%26%26%20longitude%20%3E%20%24minLng%20%26%26%20longitude%20%3C%20%24maxLng%20%26%26%20status%20%3D%3D%20%24status%20%5D%20%7Corder((%24userLat%20-%20latitude)%20**%202%20%2B%20(%24userLng%20-%20longitude)%20**%202)%5B%24offset...(%24offset%20%2B%20%24limit)%5D%20%7Blatitude%2Clongitude%2CphysicalAddress%2CrestaurantImage%7B...%2C%20asset-%3E%7D%7D&%24appEnvironemnt=%22prod%22&%24environment=%22prod%22&%24limit=100000&%24maxLat='+maxLat+'&%24maxLng='+maxLon+'&%24minLat='+minLat+'&%24minLng='+minLon+'&%24offset=0&%24status=%22Open%22&%24userLat='+userLat+'&%24userLng='+userLon

# url = 'https://locator-svc.subway.com/v3/GetLocations.ashx?callback=jQuery1111035325499733726806_1605904297062&q=%7B%22InputText%22%3A%2221.286576%2C-157.706629%22%2C%22GeoCode%22%3A%7B%22Latitude%22%3A21.286576000000004%2C%22Longitude%22%3A-157.7066295%7D%2C%22DetectedLocation%22%3A%7B%22Latitude%22%3A0%2C%22Longitude%22%3A0%2C%22Accuracy%22%3A0%7D%2C%22Paging%22%3A%7B%22StartIndex%22%3A1%2C%22PageSize%22%3A100000%7D%2C%22ConsumerParameters%22%3A%7B%22metric%22%3Afalse%2C%22culture%22%3A%22en-US%22%2C%22country%22%3A%22US%22%2C%22size%22%3A%22M%22%2C%22rtl%22%3Afalse%2C%22clientId%22%3A%2217%22%2C%22key%22%3A%22SUBWAY_PROD%22%7D%2C%22Filters%22%3A%5B%5D%2C%22LocationType%22%3A0%2C%22Stats%22%3A%7B%22abc%22%3A%5B%7B%22N%22%3A%22geo%22%2C%22R%22%3A%22A%22%7D%5D%2C%22src%22%3A%22gps%22%2C%22c%22%3A%22subwayLocator%22%7D%7D&_=1605904297064'

url = 'https://locator-svc.subway.com/v3/GetLocations.ashx?callback=jQuery1111035325499733726806_1605904297062&q=%7B%22InputText%22%3A%2221.286576%2C-157.706629%22%2C%22GeoCode%22%3A%7B%22Latitude%22%3A21.286576000000004%2C%22Longitude%22%3A-157.7066295%2C%22Accuracy%22%3Anull%2C%22CountryCode%22%3A%22%22%2C%22RegionCode%22%3Anull%2C%22PostalCode%22%3Anull%2C%22City%22%3Anull%2C%22LocalityType%22%3Anull%2C%22name%22%3Anull%7D%2C%22DetectedLocation%22%3A%7B%22Latitude%22%3A0%2C%22Longitude%22%3A0%2C%22Accuracy%22%3A0%7D%2C%22Paging%22%3A%7B%22StartIndex%22%3A1%2C%22PageSize%22%3A10%7D%2C%22ConsumerParameters%22%3A%7B%22metric%22%3Afalse%2C%22culture%22%3A%22en-US%22%2C%22country%22%3A%22US%22%2C%22size%22%3A%22M%22%2C%22template%22%3A%22%22%2C%22rtl%22%3Afalse%2C%22clientId%22%3A%2217%22%2C%22key%22%3A%22SUBWAY_PROD%22%7D%2C%22Filters%22%3A%5B%5D%2C%22LocationType%22%3A0%2C%22behavior%22%3A%22%22%2C%22FavoriteStores%22%3Anull%2C%22RecentStores%22%3Anull%2C%22Stats%22%3A%7B%22abc%22%3A%5B%7B%22N%22%3A%22geo%22%2C%22R%22%3A%22A%22%7D%5D%2C%22src%22%3A%22gps%22%2C%22act%22%3A%22%22%2C%22c%22%3A%22subwayLocator%22%7D%7D&_=1605904297064'

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

# query = {
#     'q': {"InputText":"21.286576,-157.706629","GeoCode":{"Latitude":21.286576000000004,"Longitude":-157.7066295,"Accuracy":0},"DetectedLocation":{"Latitude":0,"Longitude":0,"Accuracy":0},"Paging":{"StartIndex":1,"PageSize":100000},"ConsumerParameters":{"metric":False,"culture":"en-US","country":"US","size":"L","rtl":False,"clientId":"17","key":"SUBWAY_PROD"},"Filters":[],"LocationType":0,"Stats":{"abc":[{"N":"geo","R":"A"}],"src":"gps","c":"subwayLocator"}},

#     'callback': 'jQuery1111035325499733726806_1605904297062'
# }

response = requests.get(url, headers = req_headers).json()

print(response)

# with open('data/subway_us.json', 'w') as outfile:
#     json.dump(response, outfile)