# Simple Python Web Scraper

This is a **beginner-friendly Python web scraper** built as a first hands-on project to learn the basics of web scraping.

The scraper uses **requests** and **BeautifulSoup (bs4)** to extract book titles and prices from the website *books.toscrape.com*.

---

## What the scraper does

* Sends an HTTP request to the website
* Parses the HTML using BeautifulSoup
* Extracts:

  * Book titles (from the `title` attribute)
  * Book prices
* Prints the results to the console

This project focuses on **clean structure, correct encoding handling, and readable code**.

---

## Technologies used

* Python 3
* requests
* beautifulsoup4

---

## Possible improvements / next steps

This project is intentionally simple, but it can be extended in many ways:

* Scrape **multiple pages** (e.g. page-2, page-3, etc.)
* Store results in a **CSV or JSON file**
* Convert prices to numeric values for analysis
* Add basic error handling (timeouts, missing elements)
* Scrape additional data (ratings, availability)

---

## Disclaimer

This scraper is for **learning purposes only**.
Always check a website’s terms of service before scraping.

---

## Author

Built as a first web scraping project while learning Python.

