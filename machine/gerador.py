from gtts import gTTS
from playsound import playsound
from pathlib import Path
import subprocess

class Gerador:

    def __init__(self,text = None):
        self.home = Path.home()
        self.whats_names = ["Desktop", "Área de Trabalho"]
        self.my_folder_voz= 'vvoz'
        self.linguage = 'pt-br'
        self.text = text
        try:
            result = subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                print("FFmpeg está instalado!")
                print("Versão detectada:\n", result.stdout.splitlines()[0])
            else:
                print("FFmpeg não foi encontrado.")
        except FileNotFoundError:
            print("FFmpeg não está instalado ou não está no PATH.")


    def create_folder_voz(self):
 
        for name in self.whats_names:
            dir_path = self.home / name
            if dir_path.exists():
                folder = dir_path / self.my_folder_voz
                folder.mkdir(exist_ok=True)
                return folder

    def generate_audio(self):
        souce = self.create_folder_voz()
        audio = gTTS(
            text=self.text,
            lang = self.linguage
        )
        audio.save(f'{souce}audio_original.mp3')

    def speedup_audio(self):
        souce = self.create_folder_voz()
        speed_up = 1.5
        output_file = f'{souce}audio_padrao.mp3'

        comando = [
            "ffmpeg", "-y",
            "-i", f'{souce}audio_original.mp3',
            "-filter:a", f"atempo={speed_up}",
            "-vn", output_file
        ]

        subprocess.run(comando)
    def play_audio(self):
        playsound("voz_rapida.mp3")