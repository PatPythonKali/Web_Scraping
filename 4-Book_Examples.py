# GOAL : Get title of every book with a 2 star rating

import bs4
import requests

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
products = soup.select('.product_pod')

example = products[0]
print(example.select('a')[1]['title'])

two_star_titles = []

for n in range(1,51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select("product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = example.select('a')[1]['title']
            two_star_title.append(book_title)