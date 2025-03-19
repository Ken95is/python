import telebot
from telebot import types

bot = telebot.TeleBot('7793060635:AAGufuFWKfCP02Ki_ht3Pn-IM3iYo92U7q4')

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) # если несколько кнопок вы можете использовать row_width=2
button1 = types.KeyboardButton('Инфо о себе')

keyboard.add(button1)

@bot.message_handler(commands=['start'])
def start_message(message):
    message2 = bot.send_message(message.chat.id, 'Привет, напиши информацию о себе, я сохраню это в файлах')
    bot.register_next_step_handler(message, save_info)
    
def save_info(message):
    try:
        with open('user_info.txt', 'a') as file:
            info = message.text
            file.write(info+'\n')
    except:
        bot.send_message(message.chat.id, 'Что то пошло не так, попробуй заново!')
    else:
        bot.send_message(message.chat.id, 'Все успешно сохранилось!!!', reply_markup=keyboard)
    finally:
        print('OK')


@bot.message_handler(content_types=['text'])
def send_info(message):
    if message.text.lower() == 'инфо о себе':
        with open('user_info.txt') as file:
            bot.send_document(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, 'Нажмите на кнопку!', reply_markup=keyboard)

    
bot.polling(non_stop=True, interval=0) 