from pytube import YouTube
from model.stringFile import StringClass
from model.path import PathModel


class YoutubeController():
    def __init__(self):
        self._yt = None
        self._selectedStream = None
        self._path = PathModel()

    def _calculatePercentage(self, remaining, total):
        perc = (float(remaining) / float(total)) * 100
        return perc

    def setVideoLink(self, link=None):
        while link == None or link == '':
            link = input('Video link: ')

        self._yt = YouTube(link, on_progress_callback=self.onProgress,
                           on_complete_callback=self.onComplete)

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

    def onProgress(self, chunk, file_handle, bytes_remaining):
        # https://stackoverflow.com/questions/49185538/how-to-add-progress-bar

        size = self._selectedStream.filesize
        remaining = size - bytes_remaining
        print(size, remaining)
        print(self._calculatePercentage(remaining, size))
        # return self.percent(bytes_remaining, size)

    def onComplete(self, chunk, file_handle):

        pass

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

            auxDict = dict(itag=itag, res=res,
                           videoCodec=videoCodec, audioCodec=audioCodec)
            dataKeyValue[index] = auxDict

        return dataKeyValue
