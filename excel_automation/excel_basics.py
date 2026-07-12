import openpyxl
import pandas as pd
from openpyxl.styles import Font

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Books Data"
header_font = Font(bold=True, size=12)

ws.append (["Title", "Price", "Rating"])
for cell in ws[1]:
    cell.font = header_font
    
ws.column_dimensions["A"].width = 60
ws.column_dimensions["B"].width = 15
ws.column_dimensions["C"].width = 15
    
df = pd.read_csv("scraping/books.csv")

for index, row in df.iterrows():
    ws.append([row["Title"], row["Price"], row["Rating"]])

wb.save("excel_automation/books.xlsx")
print("saved")