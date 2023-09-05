from PySide6.QtCore import QRunnable


class Worker(QRunnable):
    def __init__(self, fn):
        super(Worker, self).__init__()
        self.fn = fn

    def run(self):
        self.fn()
