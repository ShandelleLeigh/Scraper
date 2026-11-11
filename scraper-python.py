# scraper-python.py
# To run this script, paste `python scraper-python.py` in the terminal

import bs4
import requests
import subprocess
import sys
from bs4 import BeautifulSoup

# Source - https://stackoverflow.com/a/63400620
# Posted by user12951955
# Retrieved 2026-11-10, License - CC BY-SA 4.0

url = 'https://www.scribd.com/document/625901399/Maestro-Scripting-Language'

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", bs4])


# Only scrape some pages; This has over 200 pages
page_range = [1, 5]

def get_id(num):
    return f'page{num}'

el_id = get_id(1)  # Set the initial id to 'page1'

# def get_id_selector():
#     i = 1
#     while i <= page_range[-1]:
#         print(get_id(i))
#         i += 1
        # return get_id(i)

def scrape():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # element = soup.find(id=el_id)
    element = soup.find('div', id=el_id)
    # element = soup.div[el_id]
    print(element)

if el_id == 'page1':
    scrape()