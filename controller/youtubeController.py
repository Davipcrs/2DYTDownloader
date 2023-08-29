from pytube import YouTube
from model.stringFile import StringClass
import json


class YoutubeController():
    def __init__(self):
        self._yt = None

    def setVideoLink(self, link=None):
        while link == None or link == '':
            link = input('Video link: ')

        self._yt = YouTube(link)

    def getVideoLink(self):
        if self._yt == None:
            return StringClass().noVideoSelected

        return self._yt.watch_url

    def listVideoResolutions(self):
        if self._yt == None:
            return StringClass().noVideoSelected

        streams = self._yt.streams.filter(
            type='video', file_extension='mp4').order_by(attribute_name='resolution')

        streamList = list(streams)
        auxList = []

        # Make return a JSon
        for index in range(0, streamList.__len__() - 1):
            auxList.append(streamList[index].resolution)

        return auxList

    def jsonVideoInfo(self):
        streams = self._yt.streams.filter(
            type='video', file_extension='mp4').order_by(attribute_name='resolution')

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

    def selectVideoQuality(self, itag):
        stream = self._yt.streams.get_by_itag(itag)
        stream.download()

    def onProgress():
        # https://stackoverflow.com/questions/49185538/how-to-add-progress-bar
        pass

    def onFinish():
        pass
