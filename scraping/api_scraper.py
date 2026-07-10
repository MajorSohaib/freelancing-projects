import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

result = []

for user in data:
    result.append({
        "name": user["name"],
        "email": user["email"], 
        "city": user["address"]["city"],
        "company": user["company"]["name"]
    })


import pandas as pd
df = pd.DataFrame(result)
df.to_csv("scraping/users.csv", index=False)
print("saved")