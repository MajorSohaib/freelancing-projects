#Give me all books under £20 only from https://books.toscrape.com, sorted by price lowest to highest. Deliver in excel
import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
ws = wb.active
ws.title= "Books Price Comparison"
header_font = Font(bold=True, size=12)

ws.append (["Title", "Price"])
for cell in ws[1]:
    cell.font = header_font 

data =[]

for i in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod",)
    
    for book in books:
        h3 = book.find("h3")
        name = h3.find("a")["title"]
        price_text= book.find("p", class_="price_color").get_text()
        price = float(price_text.replace("Â£", ""))
        if price < 20:
            data.append({"title": name, "price": price})
    

df = pd.DataFrame(data)
df = df.sort_values("price")

for index, row in df.iterrows():
    ws.append([row["title"], row["price"]])

wb.save("Real projects/books_price.xlsx")
print("saved")

