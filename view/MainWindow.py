import time
from PySide6.QtWidgets import QMainWindow
from view.ui.MainWindow_ui import Ui_MainWindow
from controller.youtubeController import YoutubeController
from threading import Thread


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.yt = YoutubeController()
        self.data = ''
        self.videoUrl = ''
        self.ui.confirmLinkButton.clicked.connect(self._linkUpdate)
        self.ui.videoLinkLineEdit.editingFinished.connect(self._linkUpdate)
        self.ui.downloadTypeSelectionComboBox.currentIndexChanged.connect(
            self._labelData)
        self.ui.okButton.clicked.connect(self._downloadVideo)

    def _fetchData(self):
        self.data = self.yt.jsonVideoInfo()

    def _linkUpdate(self):
        # Add A button or add a form to 'Thread' the setVideoLink
        string = self.ui.videoLinkLineEdit.text()
        if string == self.videoUrl:
            return
        self.yt.setVideoLink(link=string)
        title = self.yt.getVideoTitle()
        self.ui.videoName.setText(title)
        self.videoUrl = string

        if title != None or title != '':
            # https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/
            th = Thread(self._fetchData())
            th.start()

        self._addVideoQualityToComboBox()
        self._labelData()

        return

    def _addVideoQualityToComboBox(self):
        self.ui.downloadTypeSelectionComboBox.clear()
        aux = []
        for i in range(0, self.data.__len__() - 1):
            aux.append(self.data[i]['res'])
        self.ui.downloadTypeSelectionComboBox.addItems(aux)

    def _labelData(self):
        index = self.ui.downloadTypeSelectionComboBox.currentIndex()
        localData = self.data[index]

        self.ui.videoCodec.setText(
            'Codec de Vídeo: ' + str(localData['videoCodec']))
        self.ui.audioCodec.setText(
            'Codec de Áudio: ' + str(localData['audioCodec']))
        self.ui.downloadSize.setText('Tamanho (MB): ' + str(localData['size']))
        self.ui.audioBitrate.setText('Bitrate: ' + str(localData['bitrate']))

    def _downloadVideo(self):
        index = self.ui.downloadTypeSelectionComboBox.currentIndex()
        itag = self.data[index]['itag']

        self.yt.setVideoQuality(itag=itag)
        th = Thread(target=self.yt.downloadSelectedVideo)
        th.start()

        while self.yt.downloadComplete == False:
            print(self.yt.downloadProgress)
            time.sleep(0.8)

        print(self.yt.downloadProgress)
        print(self.yt.downloadComplete)
