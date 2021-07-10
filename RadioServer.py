#TCP_server
#coding: utf-8

import socket
import threading
import warnings
import config as c
import wave
import time
import os
from player import streamming

#warnings.filterwarnings('ignore') 

serverPort = c.portaDefault
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("Servidor em execução")

#função para verificar a existencia de um arquivo; Nome completo:verifica_existencia_arquivo.
def verificaArquivo(arq_nome):
        for path , diretorios, arqs_names in os.walk(c.diretorio_default):
                for music_name in arqs_names:
                        if arq_nome == music_name:
                                return True
        
        return False

#Inicia a reprodução das músicas.
def radio_player(rate,musica):
    playback = streamming(rate)
    playback.play(musica)

#Cria a thread que reproduz a música pelo lado do servidor.
def radio():

    musica = wave.open('/home/firulipe/Música/1.wav','rb')
    
    '''
    Convertendo o valor da taxa de reprodução(rate) que é um inteiro
    para string para poder enviar pelo socket.
    '''
    rate = str(musica.getframerate())

    thRadio = threading.Thread(target=radio_player, args=(rate,musica))
    thRadio.start()

    
    thCon = threading.Thread(target=conexoes, args=(rate,musica))
    thCon.start()

    while True:
        continue


def transmissao(connectionSocket,rate, musica):
    connectionSocket.send(rate.encode('utf-8'))

    while musica != "":
        connectionSocket.send(streamming.chunkAtual)
    
    musica.close()

#Cria threads que estabelecem conexões com cada novo cliente.
def conexoes(rate, musica):
    print("oi")
    while True:
        connectionSocket, addr = serverSocket.accept()
        print("Conexão   vinda   de  {}\n\n".format(addr))

        thTran = threading.Thread(target=transmissao, args=(connectionSocket,rate,musica))
        thTran.start()

def main():
    while True:
        radio()
        

if __name__ == '__main__':
	main()