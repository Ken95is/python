import telebot
from bs4 import BeautifulSoup as bs
import requests


bot = telebot.TeleBot('7793060635:AAGufuFWKfCP02Ki_ht3Pn-IM3iYo92U7q4')

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
button1 = telebot.types.KeyboardButton('Ноутбуки')
button2 = telebot.types.KeyboardButton('Телефоны')
keyboard.add(button1, button2)

@bot.message_handler(commands=['start'])
def start_message(message):
    message2 = bot.send_message(message.chat.id, 'Привет, я могу спарсить страницу Kivano.kg', reply_markup=keyboard)
    bot.register_next_step_handler(message2, handler)

@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text.lower() == 'телефоны':
        parsing('https://www.kivano.kg/mobilnye-telefony', message)
    elif message.text.lower() == 'ноутбуки':
        parsing('https://www.kivano.kg/noutbuki-i-kompyutery', message)
    else:
        bot.send_message(message.chat.id, 'Нажми на кнопку', reply_markup=keyboard)


def parsing(url, message):
    html = requests.get(url).text
    soup = bs(html, 'lxml')
    telephones = soup.find_all('div', class_='item product_listbox oh')
    count = 1
    for telephone in telephones:
        link = 'https://www.kivano.kg' + telephone.find('a').get('href')
        title = telephone.find('img').get('alt')
        price = telephone.find('div', class_='listbox_price text-center').text
        bot.send_message(message.chat.id, f'{count} Товар - {title}\nСсылка - {link}\nЦена - {price}', reply_markup=keyboard)
        count += 1

bot.polling(non_stop=True, interval=0)

# def parsing_laptop(url):
#     html = requests.get(url).text
#     soup = bs(html, 'lxml')
#     laptops = soup.find_all()