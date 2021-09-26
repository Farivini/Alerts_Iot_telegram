import telegram

my_token = '2025583090:AAEGG1TvDck5dOoD9g5KYV_hFFPrtPya39U'
chat_id = '-513797981'
link = 'https://cayenne.mydevices.com/cayenne/dashboard/device/0a214190-1d7a-11ec-bbfc-979c23804144'

def envia(msg, chat_id, token=my_token):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)


