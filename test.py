import requests, bs4

result = requests.get("http://www.example.com")


soup = bs4.BeautifulSoup(result.text, "lxml")

print(result.text)