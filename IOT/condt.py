import random
import time

from aviso_telegram import chat_id, my_token, envia


def temperatura():
    return random.randrange(21,35)

def umidade ():
    return random.randrange(10, 95)

def aquecedor (estado:str):
    if estado == 'on':
        envia("Aquecedor ligado",chat_id,my_token)

    if estado == 'off':
        envia("Aquecedor desligado", chat_id, my_token)
