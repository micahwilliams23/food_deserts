from bs4 import BeautifulSoup as soup
import csv
import requests
import re

base_url = 'https://locations.tacobell.com/'

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

page_html = requests.get(base_url, headers = req_headers).text

page_soup = soup(page_html, 'html.parser')

states = page_soup.findAll('a', {'class': 'Directory-listLink'})

with open('data/tacobell.csv', 'w') as f:

    writer = csv.writer(f)
    writer.writerow(['address'])

for state in states:
    
    state_url = base_url + state['href']

    requests.get(state_url, headers = req_headers)

    page_html = requests.get(state_url, headers = req_headers).text

    page_soup = soup(page_html, 'html.parser')

    cities = page_soup.findAll('a', {'class': 'Directory-listLink'})

    for city in cities:
        
        city_url = base_url + city['href']

        store_count = re.sub('\\D', '', city['data-count'])

        page_html = requests.get(city_url, headers = req_headers).text

        page_soup = soup(page_html, 'html.parser')

        if store_count == '1':

            address = page_soup.findAll('address', {'class': 'c-address'})[0].text

            with open('data/tacobell.csv', 'a') as f:

                writer = csv.writer(f)
                writer.writerow([address])

            print(address)

        else:

            addresses = page_soup.findAll('address', {'class': 'c-address'})

            with open('data/tacobell.csv', 'a') as csvfile:

                writer = csv.writer(f)

                for address in addresses:

                    writer.writerow([address.text])

                    print(address.text)