'''

 - Define two(2) functions
 - Each function makes a request to each server
    - Jumia Server
    - Kiiku Server

 - Make the soup
 - Get search item from user
 - Get the product element
 - for each product save product info

    * Title
    * Price
    * Image
    * link to product

'''

from bs4 import BeautifulSoup
import requests
import json

item = input("Enter search item: ").lower().split(" ")
search_item = "+".join(item)


def jumia(search_word):
    headers = {"User-Agent": "mozilla/5.0."}
    url = f"https://www.jumia.com.gh/catalog/?q={search_word}&sort=rating#catalog-listing"
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "lxml")
    products = soup.find_all("a", {"class": "core"})[:10]

    items_jumia = {}
    counter = 0
    for product in products:
        prod_desc = {
            "title": product.find('h3', {'class': 'name'}).text,
            "price": product.find('div', {'class': 'prc'}).text,
            "prd_link": product['href'],
            "thumbnail_link": product.find('img', {'class': 'img'})['data-src']
        }
        items_jumia[counter] = prod_desc
        counter += 1

    json_string = json.dumps(items_jumia, indent=4)
    print(json_string)


jumia(search_item)

