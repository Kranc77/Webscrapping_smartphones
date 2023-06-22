# potrzebne biblioteki
from bs4 import BeautifulSoup
import requests
import pandas as pd

''' # - przypomnienie i powtórka 
# scrapowanie kilku stron
for page in range(1, 4):

    # strona która mnie interesuje
    page = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=dodge+viper&_sacat=0&_sop=20&_pgn='+str(page))

    soup = BeautifulSoup(page.text, 'html.parser')

    # znalezienie ceny
    prices = soup.find_all('span', class_='s-item__price')
    years = soup.find_all('span', class_='s-item__dynamic s-item__dynamicAttributes1')
    mileage = soup.find_all('span', class_='s-item__dynamic s-item__dynamicAttributes2')
    # wypisanie cen bez znaczników HTML
    df = pd.DataFrame(list(zip(prices, years, mileage)))

    print(df)
'''
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

page = requests.get('https://www.x-kom.pl/g-4/c/1590-smartfony-i-telefony.html?f%5Bprice%5D%5Bfrom%5D=1000&f%5Bprice%5D%5Bto%5D=2000', headers=HEADERS)
prices = []
soup = BeautifulSoup(page.text, 'html.parser')
if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')
    prices = soup.find_all('span', class_='sc-6n68ef-0 sc-6n68ef-3 guFePW')
else:
    print(f'Błąd {page.status_code} podczas pobierania strony.')

for i in prices:
    print(i.text)