import PySimpleGUI as sg
from pytube import YouTube


class TelaPython:
    sg.theme('Default')

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

            try:
                yt = YouTube(link)
                print('Analizando...')
                print(f'Titulo: {yt.title}')
                print(f'Tempo: {yt.length} secundos')

                print(30 * '=')

                ys = yt.streams.get_highest_resolution()

                print('Downloading...')
                ys.download('Videos')
                print('Download completo!!')
            except:
                print('[ERRO] Video não encontrado no YouTube!')
            # yt = YouTube(link)


tela = TelaPython()
tela.Iniciar()
