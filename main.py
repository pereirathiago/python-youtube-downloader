from pytube import YouTube

link = input('Cole aqui o link: ')

print('Procurando seu vídeo...')
yt = YouTube(link)

print('======== Achei ========')

# Titulo do video
print(f'Título: {yt.title}')
# numero de views do video
print(f'Numero de views: {yt.views}')
# Tempo do video
print(f'Tempo: {yt.length} secundos')
# Descrição do video
print(f'Descrição do video: {yt.description}')
# Avaliação
print(f'Avaliação: {yt.rating}')

# printing todos os streams possível
# print(yt.streams)

# somente audio
# print(yt.streams.filter(only_audio=True))

# somente video
# print(yt.streams.filter(only_video=True))

# print(yt.streams.filter(progressive=True))

print(30 * '=')

ys = yt.streams.get_highest_resolution()
# ys = yt.streams.get_by_itag('22')
print('Downloading...')
ys.download('Videos')
print('Download completed!!')
