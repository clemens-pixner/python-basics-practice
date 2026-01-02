import requests 
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"
response = requests.get(url)
response.encoding = "utf-8"
html = response.text
soup = BeautifulSoup(html, "html.parser")

for article in soup.find_all("article", class_="product_pod"):
    book_name = article.h3.a["title"]
    book_price = article.find("p", class_= "price_color").get_text(strip=True)
    print(book_name)
    print(book_price)   
    print()