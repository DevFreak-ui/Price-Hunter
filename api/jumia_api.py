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
import time
from requests.exceptions import RequestException
# import json


def jumia(search_item):
    try:
        search_word = "+".join(search_item.split(" "))

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
        }
        
        url = f"https://www.jumia.com.gh/catalog/?q={search_word}&sort=rating#catalog-listing"
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, "lxml")
        products = soup.find_all("a", {"class": "core"})[:10]

        jumia_items = {}
        counter = 0
        for product in products:
            try:
                prod_desc = {
                    "title": product.find('h3', {'class': 'name'}).text.strip(),
                    "price": product.find('div', {'class': 'prc'}).text.strip(),
                    "prod_link": product['href'],
                    "thumbnail_link": product.find('img', {'class': 'img'})['data-src']
                }
                jumia_items[counter] = prod_desc
                counter += 1
            except (AttributeError, KeyError) as e:
                continue  # Skip products with missing data

        # json_string = json.dumps(jumia_items, indent=4)
        return jumia_items

    except RequestException as e:
        print(f"Error fetching data from Jumia: {str(e)}")
        return {}
    except Exception as e:
        print(f"Unexpected error in Jumia API: {str(e)}")
        return {}


