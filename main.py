# potrzebne biblioteki
from bs4 import BeautifulSoup
import requests

# strona która mnie interesuje
page = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=dodge+viper&_sacat=0&_sop=20')

soup = BeautifulSoup(page.text, 'html.parser')

# znalezienie ceny
prices = soup.find_all('span', class_='s-item__price')

# wypisanie cen bez znaczników HTML
for price in prices:
    print(price.text)

print(len(prices))