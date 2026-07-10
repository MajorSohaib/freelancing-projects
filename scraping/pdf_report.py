from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import pandas as pd

df = pd.read_csv("scraping/users.csv")

c = canvas.Canvas("scraping/users_report.pdf", pagesize=A4)
c.setFont("Helvetica-Bold", 16)
c.drawString(200, 800, "Users Report")

c.setFont("Helvetica", 12)
y = 760

for index, row in df.iterrows():
    c.drawString(50, y, f"{row['name']} | {row['email']} | {row['city']} | {row['company']}")
    y -= 30

c.save()
print(" PDF Saved")
