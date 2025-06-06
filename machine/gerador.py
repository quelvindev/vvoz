from gtts import gTTS
from playsound import playsound
from pathlib import Path
import subprocess
import os
from datetime import datetime as dt

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

    def generate_audio(self,fragment):
        souce = self.create_folder_voz()
        audio = gTTS(
            text=fragment,
            lang = self.linguage
        )
        audio.save(f'{souce}/audio_original.mp3')
        self.speedup_audio()

    def speedup_audio(self):
        source = self.create_folder_voz()
        speed_up = 1.5
        datetime = format(dt.today(),'%d_%m_%y_%H_%M_%S')
        output_file = f'{source}/{datetime}.mp3'

        comando = [
            "ffmpeg", "-y",
            "-i", f'{source}/audio_original.mp3',
            "-filter:a", f"atempo={speed_up}",
            "-vn", output_file
        ]

        subprocess.run(comando)
        os.remove(f'{source}/audio_original.mp3')
    def play_audio(self):
        source = self.create_folder_voz()
        print(source)
        with os.scandir(source) as itens:
            for item in itens:
                print(item.name)

        '''

        import os
from datetime import datetime

pasta = "sua_pasta/"
formato = "%d_%m_%y_%H_%M_%S"

mais_recente = None
data_mais_recente = None

for nome in os.listdir(pasta):
    try:
        # Tenta extrair a data do nome do arquivo (sem extensão)
        nome_sem_extensao = os.path.splitext(nome)[0]
        data = datetime.strptime(nome_sem_extensao, formato)

        if data_mais_recente is None or data > data_mais_recente:
            data_mais_recente = data
            mais_recente = nome

    except ValueError:
        # Ignora arquivos que não seguem o padrão de nome
        continue

print("Arquivo mais recente:", mais_recente)

        '''
        #playsound("voz_rapida.mp3")