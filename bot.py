import telebot

TOKEN = "8127797274:AAGRHuNgq48fg-wI8JXaXrafK4eGQNzPNZs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Saidjon qachon demoni joylaymiz?. Biror aniq javob ayt?")

    print("Bot ishga tushdi")

bot.polling()
