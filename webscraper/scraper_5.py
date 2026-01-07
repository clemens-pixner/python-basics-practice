import requests
from bs4 import BeautifulSoup
import sqlite3

def price_type(article):
    price = article.find("p", class_="price_color").get_text(strip=True)
    price_float = float(price[1:])
    return price_float

def rating_extraction(article):
    RATING_MAP = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four" : 4,
        "Five" : 5
    }
    
    rating_tag = article.find("p", class_="star-rating")
    rating_word = rating_tag["class"][1]
    return RATING_MAP[rating_word]

conn = sqlite3.connect("products.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price REAL NOT NULL,
            rating INTEGER NOT NULL,
            availability TEXT NOT NULL,
            page INTEGER NOT NULL
)
""")

page = 1

while True:
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)

    if response.status_code != 200:
        break
    
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="product_pod")

    if not articles:
        break

    for article in articles:
        title = article.h3.a["title"]
        price = price_type(article)
        rating = rating_extraction(article)
        availability = article.find("p", class_="instock availability").get_text(strip=True)

        cur.execute("""
        INSERT INTO books (title, price, rating, availability, page)
        VALUES (?, ?, ?, ?, ?)
        """, (title, price, rating, availability, page))

    page += 1

conn.commit()
conn.close()

print("Data saved to products.db")      