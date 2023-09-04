from PySide6.QtWidgets import QMainWindow, QFileDialog
from view.ui.MainWindow_ui import Ui_MainWindow
from view.DownloadDialog import DownloadDialog
from model.path import PathModel
from controller.youtubeController import YoutubeController
from threading import Thread


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.yt = YoutubeController()
        self.data = ''
        self.audioData = ''
        self.videoUrl = ''
        self.audioOnlyBool = False
        self.diferentPath = PathModel().appUsrDir
        self.downloadDialog = None

        # Handle Clicks
        self.ui.confirmLinkButton.clicked.connect(self._linkUpdate)
        self.ui.videoLinkLineEdit.editingFinished.connect(self._linkUpdate)
        self.ui.downloadTypeSelectionComboBox.currentIndexChanged.connect(
            self._labelData)
        self.ui.okButton.clicked.connect(self._downloadVideo)
        self.ui.onlyAudio.stateChanged.connect(self._audioData)
        self.ui.changeLocationButton.clicked.connect(self._changeSaveDirectory)
        self.ui.cancelButton.clicked.connect(self.close)

        self.ui.saveLocation.setText(str(self.diferentPath))

    def _fetchData(self):
        self.data = self.yt.jsonVideoInfo()

    def _fetchAudioData(self):
        self.audioData = self.yt.jsonAudioInfo()

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
            th = Thread(target=self._fetchData())
            th.start()
            th2 = Thread(target=self._fetchAudioData())
            th2.start()

        self._addVideoQualityToComboBox()
        self._labelData()

        return

    def _addVideoQualityToComboBox(self):
        self.ui.downloadTypeSelectionComboBox.clear()
        aux = []
        if self.audioOnlyBool == False:
            for i in range(0, self.data.__len__() - 1):
                aux.append(self.data[i]['res'])
            self.ui.downloadTypeSelectionComboBox.addItems(aux)
        else:
            for i in range(0, self.audioData.__len__() - 1):
                aux.append(self.data[i]['extension'])
            self.ui.downloadTypeSelectionComboBox.addItems(aux)

    def _labelData(self):
        index = self.ui.downloadTypeSelectionComboBox.currentIndex()
        if self.audioOnlyBool == False:
            localData = self.data[index]
            self.ui.videoCodec.setText(
                'Codec de Vídeo: ' + str(localData['videoCodec']))
            self.ui.audioCodec.setText(
                'Codec de Áudio: ' + str(localData['audioCodec']))
            self.ui.downloadSize.setText(
                'Tamanho (MB): ' + str(localData['size']))
            self.ui.audioBitrate.setText(
                'Bitrate: ' + str(localData['bitrate']))

        else:
            localData = self.audioData[index]
            self.ui.videoCodec.setText(
                'Codec de Vídeo: ' + 'APENAS AUDIO')
            self.ui.audioCodec.setText(
                'Codec de Áudio: ' + str(localData['audioCodec']))
            self.ui.downloadSize.setText(
                'Tamanho (MB): ' + str(localData['size']))
            self.ui.audioBitrate.setText(
                'Bitrate: ' + str(localData['bitrate']))

    def _downloadVideo(self):
        index = self.ui.downloadTypeSelectionComboBox.currentIndex()
        if self.audioOnlyBool == False:
            itag = self.data[index]['itag']
        else:
            itag = self.audioData[index]['itag']

        self.yt.setVideoQuality(itag=itag)
        th = Thread(target=self.yt.downloadSelectedVideo,
                    args=(self.diferentPath,))
        th.start()

        self.downloadDialog = DownloadDialog(self.yt, self.diferentPath)
        self.downloadDialog.show()

    def _audioData(self):
        if self.audioOnlyBool == False:
            self.audioOnlyBool = True
            self._addVideoQualityToComboBox()

            # Label data
            return
        else:
            self.audioOnlyBool = False
            self._addVideoQualityToComboBox()
            return

    def _changeSaveDirectory(self):
        self.diferentPath = QFileDialog.getExistingDirectory(
            self, 'Selecione a Pasta para salvar o arquivo.')
        if self.diferentPath == None:
            self.ui.saveLocation.setText(str(PathModel().appUsrDir))
        else:
            self.ui.saveLocation.setText(str(self.diferentPath))

        return
