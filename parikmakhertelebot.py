import telebot
# import pandas as pd
import json
from emoji import emojize

bot = telebot.TeleBot('token')

user_data = {}
with open('user_data.json', 'r', encoding = 'utf-8') as ud:
    data = json.load(ud)

@bot.message_handler(commands = ['start'])
def startwelcome(m):
    bot.send_message(m.chat.id, emojize(
        'Добро пожаловать в парикмахерскую & Beauty-салон: «Богиня красоты» :nail_polish::nail_polish::nail_polish:', 
        language = 'alias'))
    if str(m.chat.id) in data:
        str_chat_id = str(m.chat.id)
        bot.send_message(m.chat.id, f'Приветствуем вас, {data[str_chat_id]['name']}!')
    else:
        mess = bot.send_message(m.chat.id, 'Для использования бота придумайте имя для вашей учетной записи клиента. \
Введите имя для аккаунта:')
        bot.register_next_step_handler(mess, username_reg)

def username_reg(m):
    user_data[m.chat.id] = {'name': m.text}
    msg = bot.send_message(m.chat.id, 'Теперь введите ваш номер телефона (он нужен для связи с вами):')
    bot.register_next_step_handler(msg, phone_reg)

def phone_reg(m):
    user_data[m.chat.id]['phone'] = m.text
    bot.send_message(
    m.chat.id, f"Спасибо, {user_data[m.chat.id]['name']}! \
Вы успешно зарегистрированы с номером телефона: {user_data[m.chat.id]['phone']}")
    if len(user_data) > 0:
        with open('user_data.json', 'a', encoding = 'utf-8') as file:
            json.dump(user_data, file, indent = 4)

@bot.message_handler(commands = ['account'])
def my_account(m):
    str_chat_id = str(m.chat.id)
    bot.send_message(m.chat.id, f'''Имя вашего аккаунта: {data[str_chat_id]['name']}
Пароль вашего аккаунта: {data[str_chat_id]['phone']}''')

@bot.message_handler(commands = ['меню'])
def menu(m):
    pass

@bot.message_handler(commands = ['создатель'])
def creator(m):
    bot.send_message(m.chat.id, 'Меня создал <a href="https://t.me/lydemere">Владимир</a>!', parse_mode='HTML')

if __name__ == '__main__':
    print('Воркаю')
    bot.infinity_polling()
    print('До свидания!')
