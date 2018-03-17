import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/p2083183")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span",{"itemprop": "price", "class":"now-price"})
print(element.text.strip())