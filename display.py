import PySimpleGUI as sg
from pytube import YouTube
import youtube_dl
import os
import time


class TelaPython:
    sg.theme('LightBrown13')

    def __init__(self):
        layout = [
            [sg.Text('Link', size=(4, 0)), sg.Input(size=(34, 0), key='link')],
            [sg.Radio('Video', 'formato', key='video'),
             sg.Radio('Audio', 'formato', key='audio')],
            [sg.Button('Procurar video')],
            [sg.Output(size=(40, 15))]
        ]
        self.janela = sg.Window("YouTube Downloader").layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()

            link = self.values['link']
            video = self.values['video']
            audio = self.values['audio']

            print('Procurando seu vídeo...')

            if audio == False and video == False:
                print('[ERRO] Selecione uma opção(Audio/Video)')
                print(30 * '=')
            else:
                try:
                    yt = YouTube(link)
                    print('Analizando...')
                    time.sleep(3)
                    print(f'Titulo: {yt.title}')
                    print(f'Tempo: {yt.length} secundos')

                    print(30 * '=')

                    if video == True:
                        ys = yt.streams.get_highest_resolution()
                        print('Downloading...')
                        ys.download('Videos')
                    elif audio == True:
                        ys = yt.streams.get_by_itag('140')
                        print('Downloading...')
                        video_info = youtube_dl.YoutubeDL().extract_info(
                            url=link, download=False
                        )

                        path_to_save = 'Audios'

                        where_to_save = os.getcwd()
                        if path_to_save != "":
                            where_to_save = f"{path_to_save}"

                        filename = f"{video_info['title']}.mp3"
                        output_path = os.path.join(where_to_save, filename)

                        options = {
                            'format': 'bestaudio/best',
                            'keepvideo': False,
                            'outtmpl': output_path,
                            'postprocessors': [{
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': '192',
                            }]
                        }
                        with youtube_dl.YoutubeDL(options) as ydl:
                            ydl.download([video_info['webpage_url']])

                    print('Download completo!!')
                except:
                    print(
                        '[ERRO] Video não encontrado no YouTube ou erro ao baixar!')


tela = TelaPython()
tela.Iniciar()
