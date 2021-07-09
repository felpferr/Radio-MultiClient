#coding: utf-8
import config as c
import re
import pyaudio
import threading

class streamming:
    def __init__(self,Rate):
        self.ratte = int(Rate)
        self.buffer = pyaudio.PyAudio()
        self.stream = self.buffer.open(format=pyaudio.paInt32, channels=1, 
        rate=self.ratte, frames_per_buffer=4096, output=True)
        self.stream.start_stream()
    
    def play(self,musica):
        while True:
            self.stream.write(musica.readframes(4096))
            if not musica:
                self.stream.stop_stream()
                self.stream.close()
                self.buffer.terminate()
                break
    
    '''def boardEvents(self):
        while True:
            try:
                if keyboard.is_pressed('s'):
                    playback.pause()
                elif keyboard.is_pressed('p'):
                    playback.unpause()
                elif keyboard.is_pressed('l'):
                    playback.getList()
                    playback.showList()
                elif keyboard.is_pressed('e'):
                    playback.exit()
                elif keyboard.is_pressed('n'):
                    playback.new()
                else:
                    pass
            except:
                exit()
    
    def pause():
        stream.stop_stream()
    
    def unpause():
        stream.start_stream()
    
    def exit():
        stream.stop_stream()
        stream.close()
        buffer.terminate()

    def getList(self,clientSocket):
        clientSocket.send("l".encode('utf-8'))
        List = open('lista.txt','wb')
        while True:
            linha = clientSocket.recv(4096)
            List.write(linha)
            if linha == '':
                List.close()
                break  
    
    def showList():
        List = open('lista.txt')
        option = input("Pressione 1 para listar todas as músicas;\nPressione 2 \
            para filtrar a pesquisa;\n Pressione 3 para sair.")
        while True:
            if option == 1:
                linha = List.readline()
                while linha != 'EOF':
                    print(linha.split('.wav'))
                    linha = List.readline()
            elif option == 2:
                achou = 0
                letra = input("Forneça uma letra:\n")
                regexp = fr'{letra} .'
                
                print(regexp)
                 
                for l in c.letras:
                    while letra.len() >= 2:
                        letra = input('Forneça uma letra válida:')
                    
                    if letra == l:
                        achou = 1
                        print(re.findall(regexp, List))

                if achou == 0:
                    while achou == 0:
                        letra = input('Letra não encontrada ou inválida: forneça uma nova:')
                        for l in c.letras:
                            if letra == l:
                                achou = 1
                                print(re.findall(regexp, List))
            elif option == 3:
                exit()
            else:
                option = input('Opção inválida forneça uma correta:\n')    
    '''