from controller.youtubeController import YoutubeController
from threading import Thread
from PySide6.QtWidgets import QApplication
from view.MainWindow import MainWindow
import sys
import time

'''
yt = YoutubeController()
yt.setVideoLink('https://www.youtube.com/watch?v=1h_y4XsG_RA&t=15s')


info = yt.jsonAllInfo()
for i in range(0, info.__len__()):
    print(info[i], "\n")
yt.setVideoQuality(input("itag: "))

# implement THREADS
th = Thread(target=yt.downloadSelectedVideo)
th.start()


while yt.downloadComplete == False:
    print(yt.downloadProgress)
    time.sleep(0.8)

print(yt.downloadProgress)
print(yt.downloadComplete)

'''


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
