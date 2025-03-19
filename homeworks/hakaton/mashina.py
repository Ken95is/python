from bs4 import BeautifulSoup as bs
import requests
import json

URL = 'https://www.mashina.kg/'
res = requests.get(URL)

html = res.text
soup = bs(html, 'lxml')
all_cars = soup.find_all('div', class_='listing-main-block')


cars = soup.find('div', class_='category-block-content').find_all('div', 'category-block-content-item')

car_name = []
car_price = []
car_image = []

car_name_price = []
for car in cars:
    car_name.append(car.find('div', class_='main-title').text.strip())
    car_price.append(car.find('span', class_='currency-1').text.strip())
    car_image.append(car.find('img').get('src'))

count = 1
for n, p, i in zip(car_name, car_price, car_image):
    car_name_price.append({'№': count, 'Name': n, 'Price': p, 'Image': i})
    count += 1


commercial_car = soup.find('div', class_='category-block commercial').find_all('div', 'category-block-content-item')

commercial_name = []
commercial_price = []
commercial_image = []

commercial_name_price = []
for car in commercial_car:
    commercial_name.append(car.find('div', class_='main-title').text.replace('\n                                                                    ', ' ').strip())
    commercial_price.append(car.find('span', class_='currency-1').text.strip())
    commercial_image.append(car.find('img').get('src'))

count = 1
for n, p, i in zip(commercial_name, commercial_price, commercial_image):
    commercial_name_price.append({'№': count, 'Name': n, 'Price': p, 'Image': i})
    count += 1


special_car = soup.find('div', class_='category-block spec').find_all('div', 'category-block-content-item')

special_name = []
special_price = []
special_image = []

special_name_price = []
for car in special_car:
    special_name.append(car.find('div', class_='main-title').text.replace('\n                                                                    ', ' ').strip())
    special_price.append(car.find('span', class_='currency-1').text.strip())
    special_image.append(car.find('img').get('src'))

count = 1
for n, p, i in zip(special_name, special_price, special_image):
    special_name_price.append({'№': count, 'Name': n, 'Price': p, 'Image': i})
    count += 1

car_result = []

car_result.append({'Легковые ': car_name_price})
car_result.append({'Коммерческие ': commercial_name_price})
car_result.append({'Специальные ': special_name_price})

with open('mashina.json', 'a') as file:
    json.dump(car_result, file, indent=4, ensure_ascii=False)