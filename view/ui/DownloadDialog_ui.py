# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DownloadDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_downloadProgressDialog(object):
    def setupUi(self, downloadProgressDialog):
        if not downloadProgressDialog.objectName():
            downloadProgressDialog.setObjectName(u"downloadProgressDialog")
        downloadProgressDialog.resize(320, 240)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(downloadProgressDialog.sizePolicy().hasHeightForWidth())
        downloadProgressDialog.setSizePolicy(sizePolicy)
        downloadProgressDialog.setMinimumSize(QSize(320, 240))
        downloadProgressDialog.setMaximumSize(QSize(320, 240))
        self.verticalLayout = QVBoxLayout(downloadProgressDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.localSaveLabel = QLabel(downloadProgressDialog)
        self.localSaveLabel.setObjectName(u"localSaveLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.localSaveLabel.sizePolicy().hasHeightForWidth())
        self.localSaveLabel.setSizePolicy(sizePolicy1)
        self.localSaveLabel.setMinimumSize(QSize(300, 30))
        self.localSaveLabel.setMaximumSize(QSize(16777215, 30))
        self.localSaveLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.localSaveLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.downloadProgressBar = QProgressBar(downloadProgressDialog)
        self.downloadProgressBar.setObjectName(u"downloadProgressBar")
        sizePolicy1.setHeightForWidth(self.downloadProgressBar.sizePolicy().hasHeightForWidth())
        self.downloadProgressBar.setSizePolicy(sizePolicy1)
        self.downloadProgressBar.setValue(24)

        self.verticalLayout.addWidget(self.downloadProgressBar)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.okButton = QPushButton(downloadProgressDialog)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout.addWidget(self.okButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(downloadProgressDialog)

        QMetaObject.connectSlotsByName(downloadProgressDialog)
    # setupUi

    def retranslateUi(self, downloadProgressDialog):
        downloadProgressDialog.setWindowTitle(QCoreApplication.translate("downloadProgressDialog", u"Dialog", None))
        self.localSaveLabel.setText(QCoreApplication.translate("downloadProgressDialog", u"TextLabel", None))
        self.okButton.setText(QCoreApplication.translate("downloadProgressDialog", u"PushButton", None))
    # retranslateUi

