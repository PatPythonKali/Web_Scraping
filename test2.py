import requests
import bs4

res = requests.get('https://buyandsell.sulit.ph/')
soup = bs4.BeautifulSoup(res.text, 'lxml')

data_1 = soup.select(".wc-block-grid__product-title")

for x in data_1:
    print(x.text)
