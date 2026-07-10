from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import pandas as pd
df = pd.read_csv("scraping/books.csv")

c = canvas.Canvas("scraping/users_report_books.pdf", pagesize=A4)

c.setFont("Helvetica-Bold", 16)
c.drawString(200, 800, "User Report Books" )
c.setFont("Helvetica", 12)
y = 760

for index, row in df.iterrows():
    if y < 50:
        c.showPage()
        c.setFont("Helvetica", 12)
        y = 800
    c.drawString(50, y, f"{row['title']} | {row['price'].replace('Â£', 'GBP ')}") 
    y -= 30
    
c.save()
print("Pdf saved")