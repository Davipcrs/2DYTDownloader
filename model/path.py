import os
import sys
import platform


class PathModel():
    def __init__(self):
        self.home = str(os.path.expanduser('~'))
        self.videoDir = None
        self.musicDir = None
        self.appUsrDir = None

        if platform.system() == "Windows":
            self.windowsOS()

        elif platform.system() == "Linux":
            self.linuxOS()

        else:
            self.linuxOS()

    def linuxOS(self):
        self.videoDir = str(self.home + "/")
        self.musicDir = str(self.home + "/")
        self.appUsrDir = str(self.home + r"/2DYoutubeDownloader")

    def windowsOS(self):
        self.videoDir = str(self.home + "\\")
        self.musicDir = str(self.home + "\\")
        self.appUsrDir = str(self.home + r"\2DYoutubeDownloader")
