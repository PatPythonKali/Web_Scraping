import bs4
import requests

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')

# first_item = soup.select('.toctext')[0]

for item in soup.select('.toctext'):
    print(item.text)