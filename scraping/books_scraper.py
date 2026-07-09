import requests
from bs4 import BeautifulSoup
url = "http://books.toscrape.com"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")


data = []

for i in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url)
    soup  = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:   
        h3 = book.find("h3")
        name = h3.find("a")["title"]
        price = book.find("p", class_="price_color").get_text()
        rating = book.find("p", class_="star-rating")["class"][1]
        data.append({"title": name, "price": price, "rating": rating})
    
    
import pandas as pd
df = pd.DataFrame(data)
df.to_csv("scraping/books.csv", index=False)
print("saved")