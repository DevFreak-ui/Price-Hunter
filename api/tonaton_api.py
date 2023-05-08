'''

- tonaton_api.py file makes a request to tonaton website
  and retrieve a dataset of search item

'''

from bs4 import BeautifulSoup
import requests
# import json


def tonaton(search_word):
    search_word = "+".join(search_word.split(" "))
    
    headers = {"Usesr-Agent": "Mozilla/5.0"}
    base_url = f'https://tonaton.com/search?query={search_word}'
    response = requests.get(base_url, headers=headers)

    soup = BeautifulSoup(response.content, 'lxml')
    products = soup.find_all('a', {'class': 'product__item'})[:10]

    product_list = {}
    counter = 0
    for product in products:
        product_desc = {
            "title": product.find('p', {"class": "product__description"}).text,
            "price": product.find('span', {"class": "product__title"}).text,
            "location": product.find('p', {"class": "product__location"}).text,
            "prod_link": product['href'],
            "thumbnail_link": product.find('img')['src']
        }
        product_list[counter] = product_desc
        counter += 1
    
    return product_list

