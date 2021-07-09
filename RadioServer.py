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

def radio_player(rate,musica):
    playback = streamming(rate)
    playback.play(musica)

def radio():

    musica = wave.open('/home/firulipe/Música/aef.wav','rb')
    
    '''
    Convertendo o valor da taxa de reprodução(rate) que é um inteiro
    para string para poder enviar pelo socket.
    '''
    rate = str(musica.getframerate())

    radio_player(rate,musica)
    

'''def conexoes():
    while True:
        connectionSocket, addr = serverSocket.accept()
        print("Conexão   vinda   de  {}".format(addr))
        #th = threading.Thread(target)
'''
def main():
    while True:
        #th1 = threading.Thread(target=conexoes, args=())
        #th1.start()
        
        th2 = threading.Thread(target=radio, args=())
        th2.start()

        while True:
            continue
        

if __name__ == '__main__':
	main()