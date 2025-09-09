import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import pandas as pd
# url = "https://www.vanguardngr.com/latest-news/"
url = "https://jiji.ng/computers-and-laptops?price_max=120000"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
browsed = requests.get(url, headers= headers)
byChromeResponse = webdriver.Chrome()
byChromeResponse.get(url)
html= byChromeResponse.page_source
gotten = BeautifulSoup(html, 'html.parser')
# print(browsed.content)

# soup = BeautifulSoup(browsed.text,"html.parser")this is used for getting only the text

articles = gotten.select(".b-list-advert__gallery__item .qa-advert-price")
entrydate = gotten.select(".b-list-advert__gallery__item .b-advert-title-inner")
entrylink = gotten.select(".b-list-advert__gallery__item a[href]")

all_product= []
for n, m, p in zip(articles, entrydate, entrylink):
    the_title = n.text.strip()
    the_date = m.text.strip()
    the_link = f'https://jiji.ng{p['href']}'
    all_product.append({"product":the_title, "date":the_date, "link":the_link})


df= pd.DataFrame(all_product)
df.to_excel('jiji_products.xlsx',index=True)


# print(articles)