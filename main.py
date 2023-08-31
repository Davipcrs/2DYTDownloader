from controller.youtubeController import YoutubeController

yt = YoutubeController()
yt.setVideoLink('https://www.youtube.com/watch?v=1h_y4XsG_RA&t=15s')
print(yt.jsonVideoInfo())

yt.setVideoQuality(input("itag: "))
yt.downloadSelectedVideo()
# yt._yt.streams.get_audio_only('mp4').download('/home/davi/')
