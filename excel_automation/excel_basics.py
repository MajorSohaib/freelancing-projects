import openpyxl
import pandas as pd

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Books Data"
ws.append (["Title", "Price", "Rating"])

df = pd.read_csv("scraping/books.csv")

for index, row in df.iterrows():
    ws.append([row["Title"], row["Price"], row["Rating"]])

wb.save("excel_automation/books.xlsx")
print("saved")