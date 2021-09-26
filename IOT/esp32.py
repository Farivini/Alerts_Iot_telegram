import time
import paho.mqtt.client as mqtt
from conn import usuario, ss, id, server, porta
from condt import temperatura, umidade, aquecedor
from aviso_telegram import my_token, chat_id, envia

global dados

def msgs(cliente, usu, msg):
  dados = msg.payload.decode().split(',')
  aquecedor('on' if dados[1] == '1' else 'off')
  cliente.publish(f'v1/{usuario}/things/{id}/response',f'ok,{dados[0]}')



#Conexão inicial
cliente = mqtt.Client(id)
cliente.username_pw_set(usuario, ss)
cliente.connect(server, porta)
#config do botão de acionamento
#colocar um if se temp for maior ou menor

cliente.on_message = msgs
cliente.subscribe(f'v1/{usuario}/things/{id}/cmd/2')
cliente.loop_start()


while True:
    medida_tempe = temperatura()
    umiumi = umidade()
    time.sleep(10)
    cliente.publish(f'v1/{usuario}/things/{id}/data/0', medida_tempe)
    cliente.publish(f'v1/{usuario}/things/{id}/data/1', umiumi)

    time.sleep(5)
    if medida_tempe <= 27:
        envia(f'Acessar Broker para ligar Aquecedor,  Temperatura em : {medida_tempe}', chat_id, my_token)
        time.sleep(2)
        envia('https://cayenne.mydevices.com/cayenne/dashboard/device/0a214190-1d7a-11ec-bbfc-979c23804144', chat_id, my_token)
    if umiumi > 70:
        envia(f'Umidade acima de 70.  Medida atual em : {umiumi}',chat_id, my_token)
        time.sleep(2)
#cliente.disconnect()