# MutyalaHarshith Creations

import telebot
import requests
from telebot.types import InlineKeyboardButton

# Fillout Here The BotToken it gets from botfather further queries @MutyalaHarshith 0n telegram
bot = telebot.TeleBot('CAACAgUAAxkBAAIYeGK1ZXx-OIpekd6pG4JWFIT5ZPtzAAIhBgAC3ZD5V8DbuSeu9KvqHgQ')

while True:
    try:

        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton(text='Generate email'))
        keyboard.add(InlineKeyboardButton(text='Refresh inbox'))
        keyboard.add(InlineKeyboardButton(text='About'))


        @bot.message_handler(commands=['start'])
        def start_message(message):
            bot.send_message(message.chat.id,
'''
𝐻𝑒𝑦 👋,
𝑊𝑒𝑙𝑐𝑜𝑚𝑒 𝑡𝑜 𝑀𝐻 𝑇𝑒𝑚𝑃 𝑀𝑎𝑖𝑙 𝐵𝑜𝑡 💞

𝑈𝑠𝑎𝑔𝑒
➪🔥 𝑇𝑜 𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑒 𝑒𝑚𝑎𝑖𝑙𝑠 𝑏𝑦 𝑐𝑙𝑖𝑐𝑘𝑖𝑛𝑔 𝑜𝑛 𝑡ℎ𝑒 𝑏𝑢𝑡𝑡𝑜𝑛 "𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑒 𝑒𝑚𝑎𝑖𝑙"
➪🔥 𝑇𝑜 𝑟𝑒𝑓𝑟𝑒𝑠ℎ 𝑦𝑜𝑢𝑟 𝑖𝑛𝑏𝑜𝑥 𝑐𝑙𝑖𝑐𝑘 𝑜𝑛 𝑡ℎ𝑒 𝑏𝑢𝑡𝑡𝑜𝑛 "𝑅𝑒𝑓𝑟𝑒𝑠ℎ 𝑖𝑛𝑏𝑜𝑥"
➪🔥 𝐴𝑓𝑡𝑒𝑟 𝑎 𝑛𝑒𝑤 𝑙𝑒𝑡𝑡𝑒𝑟 𝑎𝑟𝑟𝑖𝑣𝑒𝑠, 𝑦𝑜𝑢 𝑤𝑖𝑙𝑙 𝑠𝑒𝑒 𝑎 𝑏𝑢𝑡𝑡𝑜𝑛 𝑤𝑖𝑡ℎ 𝑎 𝑠𝑢𝑏𝑗𝑒𝑐𝑡 𝑙𝑖𝑛𝑒, 𝑐𝑙𝑖𝑐𝑘 𝑜𝑛 𝑡ℎ𝑖𝑠 𝑏𝑢𝑡𝑡𝑜𝑛 𝑡𝑜 𝑟𝑒𝑎𝑑 𝑡ℎ𝑒 𝑚𝑒𝑠𝑠𝑎𝑔𝑒.
                              
𝐷𝑒𝑣𝑒𝑙𝑜𝑣𝑒𝑝𝑒𝑟 : @MutyalaHarshith
''',
                             reply_markup=keyboard)


        @bot.message_handler(content_types=['text'])
        def send_text(message):
            if message.text.lower() == 'generate email':
                email = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()[0]
                ekeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                ekeyboard.add(InlineKeyboardButton(text='Generate email'))
                ekeyboard.add(InlineKeyboardButton(text='Refresh inbox\n[' + str(email) + "]"))
                ekeyboard.add(InlineKeyboardButton(text='About'))
                bot.send_message(message.chat.id, "Your Temporary E-mail:")
                bot.send_message(message.chat.id, str(email), reply_markup=ekeyboard)
            elif message.text.lower() == 'refresh inbox':
                bot.send_message(message.chat.id, 'First, generate an email', reply_markup=keyboard)
            elif message.text.lower() == 'about':
                bot.send_message(message.chat.id,
'''
𝑊ℎ𝑎𝑡 𝑖𝑠 𝑀𝐻 𝑇𝑒𝑚𝑝 𝑀𝑎𝑖𝑙 💞 ?
- 𝑖𝑡 𝑖𝑠 𝑎 𝑓𝑟𝑒𝑒🔥 𝑒𝑚𝑎𝑖𝑙 𝑠𝑒𝑟𝑣𝑖𝑐𝑒 𝑡ℎ𝑎𝑡 𝑎𝑙𝑙𝑜𝑤𝑠 𝑡𝑜 𝑟𝑒𝑐𝑒𝑖𝑣𝑒 𝑒𝑚𝑎𝑖𝑙 𝑎𝑡 𝑎 𝑡𝑒𝑚𝑝𝑜𝑟𝑎𝑟𝑦 𝑎𝑑𝑑𝑟𝑒𝑠𝑠 𝑡ℎ𝑎𝑡 𝑠𝑒𝑙𝑓-𝑑𝑒𝑠𝑡𝑟𝑢𝑐𝑡𝑒𝑑 𝑎𝑓𝑡𝑒𝑟 𝑎 𝑐𝑒𝑟𝑡𝑎𝑖𝑛 𝑡𝑖𝑚𝑒 𝑒𝑙𝑎𝑝𝑠𝑒𝑠. 𝐼𝑡 𝑖𝑠 𝑎𝑙𝑠𝑜 𝑘𝑛𝑜𝑤𝑛 𝑏𝑦 𝑛𝑎𝑚𝑒𝑠 𝑙𝑖𝑘𝑒 𝑡𝑒𝑚𝑝𝑚𝑎𝑖𝑙, 10𝑚𝑖𝑛𝑢𝑡𝑒𝑚𝑎𝑖𝑙, 10𝑚𝑖𝑛𝑚𝑎𝑖𝑙, 𝑡ℎ𝑟𝑜𝑤𝑎𝑤𝑎𝑦 𝑒𝑚𝑎𝑖𝑙, 𝑓𝑎𝑘𝑒-𝑚𝑎𝑖𝑙 , 𝑓𝑎𝑘𝑒 𝑒𝑚𝑎𝑖𝑙 𝑔𝑒𝑛𝑒𝑟𝑎𝑡𝑜𝑟, 𝑏𝑢𝑟𝑛𝑒𝑟 𝑚𝑎𝑖𝑙 𝑜𝑟 𝑡𝑟𝑎𝑠ℎ-𝑚𝑎𝑖𝑙
🚀𝐻𝑜𝑤 𝐸𝑝𝑖𝑐 𝑇𝑒𝑚𝑝 𝑀𝑎𝑖𝑙 𝐵𝑒𝑐𝑜𝑚𝑒 𝑆𝑎𝑓𝑒𝑟 𝑌𝑜𝑢?⚡
- 𝑈𝑠𝑖𝑛𝑔 𝑡ℎ𝑒 𝑡𝑒𝑚𝑝𝑜𝑟𝑎𝑟𝑦 𝑚𝑎𝑖𝑙 𝑎𝑙𝑙𝑜𝑤𝑠 𝑦𝑜𝑢 𝑡𝑜 𝑐𝑜𝑚𝑝𝑙𝑒𝑡𝑒𝑙𝑦 𝑝𝑟𝑜𝑡𝑒𝑐𝑡 𝑦𝑜𝑢𝑟 𝑟𝑒𝑎𝑙 𝑚𝑎𝑖𝑙𝑏𝑜𝑥 𝑎𝑔𝑎𝑖𝑛𝑠𝑡 𝑡ℎ𝑒 𝑙𝑜𝑠𝑠 𝑜𝑓 𝑝𝑒𝑟𝑠𝑜𝑛𝑎𝑙 𝑖𝑛𝑓𝑜𝑟𝑚𝑎𝑡𝑖𝑜𝑛. 𝑌𝑜𝑢𝑟 𝑡𝑒𝑚𝑝𝑜𝑟𝑎𝑟𝑦 𝑒-𝑚𝑎𝑖𝑙 𝑎𝑑𝑑𝑟𝑒𝑠𝑠 𝑖𝑠 𝑐𝑜𝑚𝑝𝑙𝑒𝑡𝑒𝑙𝑦 𝑎𝑛𝑜𝑛𝑦𝑚𝑜𝑢𝑠. 𝑌𝑜𝑢𝑟 𝑑𝑒𝑡𝑎𝑖𝑙𝑠: 𝑖𝑛𝑓𝑜𝑟𝑚𝑎𝑡𝑖𝑜𝑛 𝑎𝑏𝑜𝑢𝑡 𝑦𝑜𝑢𝑟 𝑝𝑒𝑟𝑠𝑜𝑛 𝑎𝑛𝑑 𝑢𝑠𝑒𝑟𝑠 𝑤𝑖𝑡ℎ 𝑤ℎ𝑜𝑚 𝑦𝑜𝑢 𝑐𝑜𝑚𝑚𝑢𝑛𝑖𝑐𝑎𝑡𝑒, 𝐼𝑃-𝑎𝑑𝑑𝑟𝑒𝑠𝑠, 𝑒-𝑚𝑎𝑖𝑙 𝑎𝑑𝑑𝑟𝑒𝑠𝑠 𝑎𝑟𝑒 𝑝𝑟𝑜𝑡𝑒𝑐𝑡𝑒𝑑 𝑎𝑛𝑑 𝑐𝑜𝑚𝑝𝑙𝑒𝑡𝑒𝑙𝑦 𝑐𝑜𝑛𝑓𝑖𝑑𝑒𝑛𝑡𝑖𝑎𝑙.

➪ 𝐵𝑜𝑡 𝑁𝑎𝑚𝑒 : 𝑀𝐻 𝑇𝑒𝑚𝑝 𝑀𝑎𝑖𝑙
➪ 𝐶𝑟𝑒𝑎𝑡𝑜𝑟 : @MutyalaHarshith
➪ 𝐿𝑎𝑛𝑔𝑢𝑎𝑔𝑒 : 𝑃𝑦𝑡ℎ𝑜𝑛
➪ 𝑀𝐻𝐿𝑎𝑛𝑔𝑢𝑎𝑔𝑒 : 𝐸𝑁 | 𝑇𝐸
➪ 𝐻𝑜𝑠𝑡𝑒𝑑 : 𝐻𝑒𝑟𝑜𝑘𝑢 & 𝑂𝑘𝑡𝑒𝑡𝑜''')
            elif message.text.lower()[14] == "[":
                email = message.text.lower()[15:message.text.lower().find("]")]
                bkeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                bkeyboard.add(InlineKeyboardButton(text='Refresh inbox\n[' + str(email) + "]"))
                bkeyboard.add(InlineKeyboardButton(text='Generate email'))
                try:
                    data = requests.get(
                        "https://www.1secmail.com/api/v1/?action=getMessages&login=" + email[:email.find(
                            "@")] + "&domain=" + email[email.find("@") + 1:]).json()
                    if 'id' in data[0]:
                        for i in range(len(data)):
                            id = data[i]['id']
                            subject = data[i]['subject']
                            fromm = data[i]['from']
                            date = data[i]['date']
                            if len(subject) > 15:
                                subject = str(subject[0:15]) + "..."
                            bkeyboard.add(InlineKeyboardButton(
                                text=str(subject) + "\n from: " + fromm + " in " + "[id" + str(id) + "][" + str(
                                    email) + "]"))
                            bot.send_message(message.chat.id,
                                             "Subject: " + subject + "\n From: " + fromm + "\n Date:" + date,
                                             reply_markup=bkeyboard)
                            count = i + 1
                        bot.send_message(message.chat.id, "Here " + str(
                            count) + " message we're found\nClick on the below button to read the message\n\n Further Queries @MHGcHaT")
                    else:
                        bot.send_message(message.chat.id, 'Nothing found', reply_markup=bkeyboard)
                except BaseException:
                    bot.send_message(message.chat.id, 'No messages were received...', reply_markup=bkeyboard)
            elif message.text.lower().find("[id"):
                try:
                    data = message.text.lower()[message.text.lower().find("[id"):]
                    id = data[data.find("[") + 3:data.find(']')]
                    email = data[data.find("][") + 2:-1]
                    msg = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login=" + email[:email.find(
                        "@")] + "&domain=" + email[email.find("@") + 1:] + "&id=" + id).json()
                    bot.send_message(message.chat.id,
                                     'Message ✉️\n\n   From: ' + msg['from'] + "\n   Subject: " + msg[
                                         'subject'] + "\n   Date: " + msg[
                                         'date'] + "\n   text: " + msg['textBody'])
                except BaseException:
                    pass


        bot.polling(none_stop=True, interval=1, timeout=5000)
    except BaseException:
        pass
        
#MutyalaHarshith Develoveper Created By కృత్రిమ మేధస్సు 2022 
