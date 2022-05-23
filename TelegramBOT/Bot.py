import telebot
import requests
API_TOKEN = '<YOUR_TOKEN>'

bot = telebot.TeleBot(API_TOKEN)

search_url = 'https://api.xrel.to/v2/search/releases.json'
error_20 = {'error': 'No results found', 'error_code': 20}
xrel_error = {'total': 0, 'results': []}


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, this is a rel checker tpye /chk <moviename>
Use . instead of space\
""")

@bot.message_handler(commands=['chk'])
def rel_check(message):
    
    
    a = message.text.split(' ')[1]
    b = a.replace(" ", ".")
    params = {
    'q': b,
    'limit': "2",
}
    x = requests.get(search_url, params=params).json()
    if x == xrel_error:
        bot.reply_to(message, "No releases found on xrel.to")
    else:    
        bot.reply_to(message, x["results"][0]["dirname"]+"\n"+"Link to release:""\n"+x["results"][0]["ext_info"]["link_href"])

bot.infinity_polling()
