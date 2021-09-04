import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text, 'lxml')

image = soup.select('.thumbimage')

computer = soup.select('.thumbimage')[0]['src']
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')

f = open('my_computer_image.jpg', 'wb')
f.write(image_link.content)
f.close()