import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/p2083183")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span",{"itemprop": "price", "class":"now-price"})
string_prince = element.text.strip()
price_without_symbol = string_prince[1:]
price = float(price_without_symbol)

if price > 200:
    print("At {} this chair is too expensive!".format(string_prince))
elif 200 > price > 100:
    print("At {} this chair is affordable".format(string_prince))
else:
    print("At {} this chair is rubbish, don't buy it!".format(string_prince))