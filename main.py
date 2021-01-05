from pytube import YouTube

link = input('Cole o link aqui: ')
yt = YouTube(link)

# Titulo do video
print(f'Título: {yt.title}')
