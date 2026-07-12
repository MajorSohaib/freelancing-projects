import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://realpython.com/jobs/"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")
jobs = soup.find_all("div", class_="alert alert-primary")

data =[]
for Job in jobs:
    title = Job.find("strong").get_text()
    Discription = Job.find("p").get_text()
    Discription = Discription.replace(title, "").strip()
    data.append({"Job": title, "Discription": Discription})
    

df = pd.DataFrame(data)
df.to_csv("Real projects/jobs.csv", index=False)
print("saved")
