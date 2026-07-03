import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "http://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
print(len(books))