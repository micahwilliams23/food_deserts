from bs4 import BeautifulSoup as soup
import requests

url = 'https://www.yelp.com/search?choq=1&find_desc=McDonald%27s&find_loc=Honolulu%2C+HI'

page_html = requests.get(url).content

page_soup = soup(page_html, 'html.parser')

container = page_soup.findAll('div', {'class': 'scrollablePhotos__373c0__1LEvd'})

site = {
    'name': container[0].findAll('a', {'class': 'link-size--inherit__373c0__1VFlE'})[0].text,
    'address': container[0].findAll('address')[0].text
}

print(site)