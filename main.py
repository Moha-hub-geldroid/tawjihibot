import telebot
import requests,time

bot = telebot.TeleBot("5992014999:AAFUHzhsqEIf223bdBX9GcsZtESE41fa0-Y")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,text="Waiting for response ...\n\nwhen site opens you will be notified")
    for i in range(999999999999):
        url = "https://www.tawjihi.jo/"
        try:
            req = requests.get(url)
            bot.send_message(message.chat.id,"Site is opened now ...\n\nLink : https://www.tawjihi.jo/")
            time.sleep(2)
            exit()
        except:
            bot.send_message(5939336463,Exception)
        time.sleep(3)

    
bot.polling()
