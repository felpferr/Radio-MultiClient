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
            self.stream.write(musica)
            if not musica:
                self.stream.stop_stream()
                self.stream.close()
                self.buffer.terminate()
                break