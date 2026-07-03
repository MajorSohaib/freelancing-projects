import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")

data = []
for quote in quotes:
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    tag = quote.find_all("a", class_="tag")
    tag_list = [t.get_text() for t in tag]
    data.append({"quote": text, "author": author, "tag":tag_list})
    
   

df = pd.DataFrame(data)
df.to_csv("scraping/quotes.csv", index=False)
print("saved")

