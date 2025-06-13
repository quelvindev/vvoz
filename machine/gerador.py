from gtts import gTTS
from playsound import playsound
from pathlib import Path
import subprocess
import os
import pygame
from datetime import datetime as dt

class Gerador:

    def __init__(self,text = None):
        self.home = Path.home()
        self.whats_names = ["Desktop", "Área de Trabalho"]
        self.my_folder_voz= 'vvoz'
        self.linguage = 'pt-br'
        self.text = text
        self.datetime = None
        self.istalffmeg = None
        try:
            result = subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                #print("FFmpeg está instalado!")
                #print("FFmpeg está instalado! Versão detectada:\n", result.stdout.splitlines()[0])
                self.istalffmeg = "FFmpeg está instalado! FFmpeg está instalado! Versão detectada:\n", result.stdout.splitlines()[0]
            else:
                #print("FFmpeg não foi encontrado.")
                self.istalffmeg = "FFmpeg não foi encontrado."
        except FileNotFoundError:
            # print("FFmpeg não está instalado ou não está no PATH.")
            self.istalffmeg = "FFmpeg não está instalado ou não está no PATH."
        pygame.init()
        pygame.mixer.init()


    def create_folder_voz(self):
 
        for name in self.whats_names:
            dir_path = self.home / name
            if dir_path.exists():
                folder = dir_path / self.my_folder_voz
                folder.mkdir(exist_ok=True)
                return folder

    def generate_audio(self,fragment,speed_up):
        souce = self.create_folder_voz()
        audio = gTTS(
            text=fragment,
            lang = self.linguage
        )
        audio.save(f'{souce}/audio_original.mp3')
        self.speedup_audio(speed_up)

    def speedup_audio(self,speed_up = 1.5):
        source = self.create_folder_voz()
        
        self.datetime = format(dt.today(),'%d_%m_%y_%H_%M_%S')
        output_file = f'{source}/{self.datetime}.mp3'

        comando = [
            "ffmpeg", "-y",
            "-i", f'{source}/audio_original.mp3',
            "-filter:a", f"atempo={speed_up}",
            "-vn", output_file
        ]

        subprocess.run(comando)
        os.remove(f'{source}/audio_original.mp3')
        return self.datetime
    def play_audio(self):
        source = self.create_folder_voz()
        pygame.mixer.music.load(f'{source}/{self.datetime}.mp3')
        pygame.mixer.music.play()

    def pause_audio(self):
        pygame.mixer.music.pause()

    def unpause_audio(sefl):
        pygame.mixer.music.unpause()

    def stop_audio(self):
        pygame.mixer.music.stop()