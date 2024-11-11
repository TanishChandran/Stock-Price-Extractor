import requests
from bs4 import BeautifulSoup
import time

ticker = 'ZOMATO'
url = f'https://www.google.com/finance/quote/{ticker}:NSE'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

class1 = 'YMlKec fxKbKc'
price = float(soup.find(class_ = class1).text.strip()[1:].replace(',',""))
for i in range(3):
    print(price)
    time.sleep(5)
