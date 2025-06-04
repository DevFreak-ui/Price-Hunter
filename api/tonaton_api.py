'''

- tonaton_api.py file makes a request to tonaton website
  and retrieve a dataset of search item

'''

from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
# import json


def tonaton(search_word):
    try:
        search_word = "+".join(search_word.split(" "))
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
        }
        
        base_url = f'https://tonaton.com/search?query={search_word}'
        response = requests.get(base_url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'lxml')
        products = soup.find_all('a', {'class': 'product__item'})[:10]

        product_list = {}
        counter = 0
        for product in products:
            try:
                product_desc = {
                    "title": product.find('p', {"class": "product__description"}).text.strip(),
                    "price": product.find('span', {"class": "product__title"}).text.strip(),
                    "location": product.find('p', {"class": "product__location"}).text.strip(),
                    "prod_link": product['href'],
                    "thumbnail_link": product.find('img')['src']
                }
                product_list[counter] = product_desc
                counter += 1
            except (AttributeError, KeyError) as e:
                continue  # Skip products with missing data
        
        return product_list

    except RequestException as e:
        print(f"Error fetching data from Tonaton: {str(e)}")
        return {}
    except Exception as e:
        print(f"Unexpected error in Tonaton API: {str(e)}")
        return {}

