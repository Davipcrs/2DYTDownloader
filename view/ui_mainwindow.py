# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'MainWindow.ui'
##
# Created by: Qt User Interface Compiler version 6.5.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
                               QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                               QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
                               QStatusBar, QVBoxLayout, QWidget)
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.videoLinkLineEdit = QLineEdit(self.centralwidget)
        self.videoLinkLineEdit.setObjectName(u"videoLinkLineEdit")

        self.verticalLayout.addWidget(self.videoLinkLineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.videoName = QLabel(self.groupBox)
        self.videoName.setObjectName(u"videoName")

        self.verticalLayout_3.addWidget(self.videoName)

        self.downloadSize = QLabel(self.groupBox)
        self.downloadSize.setObjectName(u"downloadSize")

        self.verticalLayout_3.addWidget(self.downloadSize)

        self.audioCodec = QLabel(self.groupBox)
        self.audioCodec.setObjectName(u"audioCodec")

        self.verticalLayout_3.addWidget(self.audioCodec)

        self.videoCodec = QLabel(self.groupBox)
        self.videoCodec.setObjectName(u"videoCodec")

        self.verticalLayout_3.addWidget(self.videoCodec)

        self.horizontalLayout_2.addWidget(self.groupBox)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.downloadTypeSelection = QComboBox(self.centralwidget)
        self.downloadTypeSelection.setObjectName(u"downloadTypeSelection")

        self.verticalLayout_2.addWidget(self.downloadTypeSelection)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.changeLocationButton = QPushButton(self.centralwidget)
        self.changeLocationButton.setObjectName(u"changeLocationButton")

        self.verticalLayout_4.addWidget(self.changeLocationButton)

        self.verticalSpacer_4 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.saveLocation = QLabel(self.centralwidget)
        self.saveLocation.setObjectName(u"saveLocation")

        self.verticalLayout_4.addWidget(self.saveLocation)

        self.verticalSpacer_2 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.onlyAudio = QCheckBox(self.centralwidget)
        self.onlyAudio.setObjectName(u"onlyAudio")

        self.verticalLayout_4.addWidget(self.onlyAudio)

        self.verticalSpacer = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.downloadBestQuality = QCheckBox(self.centralwidget)
        self.downloadBestQuality.setObjectName(u"downloadBestQuality")

        self.verticalLayout_4.addWidget(self.downloadBestQuality)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_3.addWidget(self.cancelButton)

        self.okButton = QPushButton(self.centralwidget)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout_3.addWidget(self.okButton)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout_5.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate(
            "MainWindow", u"GroupBox", None))
        self.videoName.setText(QCoreApplication.translate(
            "MainWindow", u"TextLabel", None))
        self.downloadSize.setText(QCoreApplication.translate(
            "MainWindow", u"TextLabel", None))
        self.audioCodec.setText(QCoreApplication.translate(
            "MainWindow", u"TextLabel", None))
        self.videoCodec.setText(QCoreApplication.translate(
            "MainWindow", u"TextLabel", None))
        self.changeLocationButton.setText(
            QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.saveLocation.setText(QCoreApplication.translate(
            "MainWindow", u"TextLabel", None))
        self.onlyAudio.setText(QCoreApplication.translate(
            "MainWindow", u"CheckBox", None))
        self.downloadBestQuality.setText(
            QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.cancelButton.setText(QCoreApplication.translate(
            "MainWindow", u"PushButton", None))
        self.okButton.setText(QCoreApplication.translate(
            "MainWindow", u"PushButton", None))
    # retranslateUi
