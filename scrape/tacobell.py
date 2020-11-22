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

with open('data/tacobell.csv', 'w', newline = '') as f:

    writer = csv.writer(f)
    writer.writerow(['street', 'city', 'state', 'zip_code'])

for state in states:
    
    state_url = base_url + state['href']

    page_html = requests.get(state_url, headers = req_headers).text

    page_soup = soup(page_html, 'html.parser')

    cities = page_soup.findAll('a', {'class': 'Directory-listLink'})

    for city in cities:
        
        city_url = base_url + city['href']

        page_html = requests.get(city_url, headers = req_headers).text

        page_soup = soup(page_html, 'html.parser')

        addresses = page_soup.findAll('address', {'class': 'c-address'})

        with open('data/tacobell.csv', 'a', newline = '') as f:
                
            writer = csv.writer(f)

            for address in addresses:

                street = address.find('span', {'class':'c-address-street-1'}).text
                city = address.find('span', {'class':'c-address-city'}).text
                state = address.find('abbr', {'class':'c-address-state'}).text
                zip_code = address.find('span', {'class':'c-address-postal-code'}).text

                writer.writerow([street, city, state, zip_code])

                print(street+','+city+','+state+','+zip_code)

