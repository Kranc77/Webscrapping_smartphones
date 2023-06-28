# potrzebne biblioteki
from bs4 import BeautifulSoup
import requests
import pandas as pd
import random

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
# dodanie wielu agentów
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36']

# strona z której są dane
df = pd.DataFrame(columns=['name', 'price'])
for i in range(1,4):
    page = requests.get('https://www.x-kom.pl/g-4/c/1590-smartfony-i-telefony.html?page='+str(i)+'&f%5Bprice%5D%5Bfrom%5D=1000&f%5Bprice%5D%5Bto%5D=2000&f192-pamiec-ram=105773-8-gb&f192-pamiec-ram=135440-12-gb&f193-pamiec-wbudowana=27930-128-gb&f193-pamiec-wbudowana=75863-256-gb&f197-lacznosc=70098-5g',
                        headers={'User-Agent': random.choice(user_agents_list)})
    soup = BeautifulSoup(page.text, 'html.parser')
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        prices = soup.find_all('span', class_='sc-6n68ef-0 sc-6n68ef-3 guFePW')
        name = soup.find_all('h3', class_='sc-16zrtke-0 kGLNun sc-1yu46qn-9 feSnpB')
        df = pd.concat([df, pd.DataFrame({"name":list(name), "price":list(prices)})], ignore_index=True)
        print(i)
    else:
        print(f'Błąd {page.status_code} podczas pobierania strony.')


print(df)
df.to_csv('raw_data.csv', index=False)

