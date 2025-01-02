import telebot

token = 'токен'

bot = telebot.TeleBot(token)
f='Это не слово "word"'

@bot.message_handler(content_types=["text"])
def echo(message):
    if 'word' in message.text:
        bot.send_message(message.chat.id, message.text)
    else:
        bot.send_message(message.chat.id, f)


bot.polling(none_stop=True)