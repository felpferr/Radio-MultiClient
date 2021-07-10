#TCPclient
#coding: utf-8

import socket
import config as c
import threading
import pyaudio
from playerCliente import streamming
import warnings
import time

warnings.filterwarnings('ignore')

serverName = '127.0.0.1'
serverPort = c.portaDefault

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def radio_player(rate,musica):
    playback = streamming(rate)
    playback.play(musica)

def main():
    rate = clientSocket.recv(1024).decode('utf-8')
    musica = clientSocket.recv(4096)

    radio_player(rate,musica)
    
if __name__ == '__main__':
	main()