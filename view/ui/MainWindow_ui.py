# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(500, 540))
        MainWindow.setMaximumSize(QSize(500, 540))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.videoLinkLineEdit = QLineEdit(self.centralwidget)
        self.videoLinkLineEdit.setObjectName(u"videoLinkLineEdit")

        self.horizontalLayout_4.addWidget(self.videoLinkLineEdit)

        self.confirmLinkButton = QPushButton(self.centralwidget)
        self.confirmLinkButton.setObjectName(u"confirmLinkButton")

        self.horizontalLayout_4.addWidget(self.confirmLinkButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.infoGroup = QGroupBox(self.centralwidget)
        self.infoGroup.setObjectName(u"infoGroup")
        self.verticalLayout_3 = QVBoxLayout(self.infoGroup)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.videoName = QLabel(self.infoGroup)
        self.videoName.setObjectName(u"videoName")
        self.videoName.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.videoName)

        self.downloadSize = QLabel(self.infoGroup)
        self.downloadSize.setObjectName(u"downloadSize")
        self.downloadSize.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.downloadSize)

        self.audioCodec = QLabel(self.infoGroup)
        self.audioCodec.setObjectName(u"audioCodec")
        self.audioCodec.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.audioCodec)

        self.videoCodec = QLabel(self.infoGroup)
        self.videoCodec.setObjectName(u"videoCodec")
        self.videoCodec.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.videoCodec)

        self.audioBitrate = QLabel(self.infoGroup)
        self.audioBitrate.setObjectName(u"audioBitrate")
        self.audioBitrate.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.audioBitrate)


        self.horizontalLayout_2.addWidget(self.infoGroup)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.onlyAudio = QCheckBox(self.centralwidget)
        self.onlyAudio.setObjectName(u"onlyAudio")

        self.verticalLayout_2.addWidget(self.onlyAudio)

        self.downloadBestQuality = QCheckBox(self.centralwidget)
        self.downloadBestQuality.setObjectName(u"downloadBestQuality")

        self.verticalLayout_2.addWidget(self.downloadBestQuality)

        self.downloadTypeSelectionComboBox = QComboBox(self.centralwidget)
        self.downloadTypeSelectionComboBox.setObjectName(u"downloadTypeSelectionComboBox")

        self.verticalLayout_2.addWidget(self.downloadTypeSelectionComboBox)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.changeLocationButton = QPushButton(self.centralwidget)
        self.changeLocationButton.setObjectName(u"changeLocationButton")

        self.verticalLayout_4.addWidget(self.changeLocationButton)

        self.saveLocation = QLabel(self.centralwidget)
        self.saveLocation.setObjectName(u"saveLocation")
        self.saveLocation.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.saveLocation)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
        self.menubar.setGeometry(QRect(0, 0, 500, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.confirmLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link", None))
        self.infoGroup.setTitle(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.videoName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.downloadSize.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.audioCodec.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.videoCodec.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.audioBitrate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.onlyAudio.setText(QCoreApplication.translate("MainWindow", u"Apenas \u00e1udio", None))
        self.downloadBestQuality.setText(QCoreApplication.translate("MainWindow", u"Melhor Qualidade", None))
        self.changeLocationButton.setText(QCoreApplication.translate("MainWindow", u"Salvar Como", None))
        self.saveLocation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.okButton.setText(QCoreApplication.translate("MainWindow", u"Baixar", None))
    # retranslateUi

