import requests
from bs4 import BeautifulSoup
import csv

url = "https://github.com/trending"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

repos = soup.find_all("article", class_="Box-row")[:5]

data = []
for repo in repos:
    full_name = repo.h2.a.get_text(strip=True).replace("\n", "").replace(" ", "")
    link = "https://github.com" + repo.h2.a["href"]
    data.append([full_name, link])

with open("trending.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["repository_name", "link"])
    writer.writerows(data)

print("Top 5 trending repositories saved to trending.csv")
