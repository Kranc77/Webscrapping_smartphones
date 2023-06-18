from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=dodge+viper&_sacat=0&_sop=20')

soup = BeautifulSoup(page.text, 'html.parser')