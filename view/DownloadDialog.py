import time
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QRunnable, QThreadPool
from view.ui.DownloadDialog_ui import Ui_downloadProgressDialog
import os


class DownloadDialog(QWidget):
    def __init__(self, stream, path):
        super(DownloadDialog, self).__init__()
        self.ui = Ui_downloadProgressDialog()
        self.ui.setupUi(self)
        self.stream = stream
        self.path = path
        self.ui.localSaveLabel.setText(str(self.path))

        self.ui.okButton.clicked.connect(self._openFile)

        self._threadedFunction()

    def _progressBarControll(self):
        self.ui.downloadProgressBar.setValue(0)

        while self.stream.downloadComplete == False:
            self.ui.downloadProgressBar.setValue(
                int(self.stream.downloadProgress[0]))
            # print(self.stream.downloadProgress)
            time.sleep(0.8)

        self.ui.downloadProgressBar.setValue(100)
        return

    def _threadedFunction(self):
        self.threadpool = QThreadPool()
        worker = Worker(self._progressBarControll)

        self.threadpool.start(worker)

    def _openFile(self):
        # Implement a way to open the file explorer
        self.close()
        pass


class Worker(QRunnable):
    def __init__(self, fn):
        super(Worker, self).__init__()
        self.fn = fn

    def run(self):
        self.fn()
