import pdfplumber
import pandas as pd

data = []

with pdfplumber.open("scraping/users_report.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        lines = text.split("\n")
        for line in lines:
            parts = line.split(" | ")
            if len(parts) == 4:
                data.append({
                "name" : parts[0], 
                "email" : parts[1],
                "city" : parts[2],
                "company" : parts[3]
            
            })
            
df = pd.DataFrame(data)
df.to_csv("pdf_extraction/users_from_pdf.csv", index=False)
print("saved")



     
        
        