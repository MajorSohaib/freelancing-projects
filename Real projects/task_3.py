#Extract only Albert Einstein quotes from https://quotes.toscrape.com — not other authors. Deliver in CSV with quote text and tags."

import requests 
import pandas as pd
from bs4 import BeautifulSoup
url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")

data =[]

for i in range(1, 11):
    url = f"http://quotes.toscrape.com/page/{i}/"
    response=requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    
    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        tag = quote.find_all("a", class_="tag")
        tag_list = [t.get_text() for t in tag]
        
        
        if author == "Albert Einstein":
            data.append({"quote": text, "tags": tag_list})


df = pd.DataFrame(data)
df.to_csv("Real projects/task_3.py.csv", index=False)
print("saved")
