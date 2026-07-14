import pdfplumber
import pandas as pd

data = []

with pdfplumber.open("scraping/users_report_books.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        lines = text.split("\n")
        for line in lines:
            if " | " in line:
                parts = line.split(" | ")
                data.append({
                "Title":parts [0],
                "Price":parts[1]
            })
            
           
            
df = pd.DataFrame(data)
df.to_csv("pdf_extraction/books_from_pdf.csv", index=False)
print("saved")  
          
        