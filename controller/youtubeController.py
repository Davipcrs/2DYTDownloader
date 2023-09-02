from pytube import YouTube
from model.stringFile import StringClass
from model.path import PathModel


class YoutubeController():
    def __init__(self):
        # Class Variables
        self._yt = None
        self._selectedStream = None
        self._path = PathModel()

        # Download Handlers
        self.downloadProgress = [0, 0, 0]
        self.downloadComplete = False

    # ================ #
    # Internal Methods
    def _calculatePercentage(self, remaining, total):
        perc = (float(remaining) / float(total)) * 100
        return perc

    def _onProgress(self, chunk, file_handle, bytes_remaining):
        size = self._selectedStream.filesize
        remaining = size - bytes_remaining
        self.downloadProgress[0] = self._calculatePercentage(remaining, size)
        self.downloadProgress[1] = size
        self.downloadProgress[2] = remaining

    def _onComplete(self, chunk, file_handle):
        self.downloadComplete = True

    # ================ #
    # External Methods
    def setVideoLink(self, link=None):
        while link == None or link == '':
            link = input('Video link: ')

        self._yt = YouTube(link, on_progress_callback=self._onProgress,
                           on_complete_callback=self._onComplete)

    def getVideoLink(self):
        if self._yt == None:
            return StringClass().noVideoSelected

        return self._yt.watch_url

    def setVideoQuality(self, itag):
        self._selectedStream = self._yt.streams.get_by_itag(itag)

    def getSelectedVideoQuality(self):
        if self._selectedStream != None:
            return self._selectedStream.resolution

    def getSelectedVideoCodecs(self):
        if self._selectedStream != None:
            return self._selectedStream.codecs

    def downloadSelectedVideo(self, path=None):
        if self._selectedStream == None:
            return StringClass().noVideoQuality

        if path == None:
            path = self._path
            path = path.appUsrDir

        self._selectedStream.download(path)

    def jsonVideoInfo(self):
        streams = self._yt.streams.filter(
            type='video').order_by(attribute_name='resolution')

        streamList = list(streams)
        dataKeyValue = {}
        index = 0

        for index in range(0, streamList.__len__() - 1):
            itag = streamList[index].itag
            res = streamList[index].resolution
            videoCodec = streamList[index].video_codec
            audioCodec = streamList[index].audio_codec
            extension = streamList[index].subtype
            size = streamList[index].filesize_mb

            auxDict = dict(itag=itag, res=res, extension=extension,
                           videoCodec=videoCodec, audioCodec=audioCodec, size=size)
            dataKeyValue[index] = auxDict

        return dataKeyValue

    def jsonAudioInfo(self):
        streams = self._yt.streams.filter(
            only_audio=True)

        streamList = list(streams)
        dataKeyValue = {}
        index = 0

        for index in range(0, streamList.__len__() - 1):
            itag = streamList[index].itag
            audioCodec = streamList[index].audio_codec
            size = streamList[index].filesize_mb
            extension = streamList[index].subtype

            auxDict = dict(itag=itag, extension=extension,
                           audioCodec=audioCodec, size=size)
            dataKeyValue[index] = auxDict

        return dataKeyValue

    def jsonAllInfo(self):
        aux1 = self.jsonVideoInfo()
        aux2 = self.jsonAudioInfo()
        # | is a Dict Merge operator
        aux3 = aux1 | aux2

        return aux3
