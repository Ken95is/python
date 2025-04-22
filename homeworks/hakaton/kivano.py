from bs4 import BeautifulSoup as bs
import requests
import json

URL = 'https://www.kivano.kg/mobilnye-telefony?page=2'
res = requests.get(URL)

html = res.text
soup = bs(html, 'lxml')
telephones = soup.find_all('div', class_='item product_listbox oh')

title = []
price = []
image = []

for telephone in telephones:
    title.append(telephone.find('a').get('href'))
    image.append(telephone.find('img').get('src'))
    price.append(telephone.find('div', class_='listbox_price text-center').text.replace('<strong>', '***').replace('\n', '').strip('***'))
    tel = list(zip(title, price, image))

with open('kiv.json', 'w', encoding='utf-8') as file:
    json.dump(tel, file, indent=4, ensure_ascii=False)
