'''

 - Define two(2) functions
 - Each function makes a request to each server
    - Jumia Server
    - Tonaton Server

 - Prepare the soup
 - Get search item from user
 - Access product element from the parser
 - for each product, define a dictionary & store product info

    * Title
    * Price
    * Image
    * link to product

'''

from bs4 import BeautifulSoup
import requests
# import json


def jumia(search_item):
    search_word = "+".join(search_item.split(" "))

    headers = {"User-Agent": "mozilla/5.0."}
    url = f"https://www.jumia.com.gh/catalog/?q={search_word}&sort=rating#catalog-listing"
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "lxml")
    products = soup.find_all("a", {"class": "core"})[:10]

    jumia_items = {}
    counter = 0
    for product in products:
        prod_desc = {
            "title": product.find('h3', {'class': 'name'}).text.strip(),
            "price": product.find('div', {'class': 'prc'}).text.strip(),
            "prod_link": product['href'],
            "thumbnail_link": product.find('img', {'class': 'img'})['data-src']
        }
        jumia_items[counter] = prod_desc
        counter += 1

    # json_string = json.dumps(jumia_items, indent=4)
    return jumia_items


