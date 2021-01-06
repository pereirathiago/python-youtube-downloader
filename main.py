from pytube import YouTube

link = input('Cole aqui o link: ')
yt = YouTube(link)

# Titulo do video
print(f'Título: {yt.title}')
