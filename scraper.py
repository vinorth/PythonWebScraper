from bs4 import BeautifulSoup
import requests

url = 'http://econpy.pythonanywhere.com/ex/001.html'

res = requests.get(url, timeout=5)

page_content = BeautifulSoup(res.content, "html.parser")

prices = page_content.find_all(class_='item-price')

print(prices)