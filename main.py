from controller.youtubeController import YoutubeController

yt = YoutubeController()
yt.setVideoLink('https://www.youtube.com/watch?v=1h_y4XsG_RA&t=15s')


info = yt.jsonAudioInfo()
for i in range(0, info.__len__()):
    print(info[i], "\n")
yt.setVideoQuality(input("itag: "))

# implement THREADS

yt.downloadSelectedVideo()
yt.downloadProgress

# yt._yt.streams.get_audio_only('mp4').download('/home/davi/')
