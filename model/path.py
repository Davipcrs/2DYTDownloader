import os
import sys


class PathModel():
    def __init__(self):
        self.home = str(os.path.expanduser())
