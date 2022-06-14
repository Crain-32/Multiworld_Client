# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'multiworldClient.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QLabel,
                               QLineEdit, QListWidget, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 325)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(850, 325))
        MainWindow.setMaximumSize(QSize(850, 325))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dialogLog = QListWidget(self.centralwidget)
        self.dialogLog.setObjectName(u"dialogLog")
        self.dialogLog.setGeometry(QRect(330, 20, 500, 280))
        self.dialogLog.setFocusPolicy(Qt.NoFocus)
        self.serverButton = QPushButton(self.centralwidget)
        self.serverButton.setObjectName(u"serverButton")
        self.serverButton.setGeometry(QRect(90, 240, 75, 25))
        self.serverIpInput = QLineEdit(self.centralwidget)
        self.serverIpInput.setObjectName(u"serverIpInput")
        self.serverIpInput.setGeometry(QRect(90, 90, 120, 20))
        self.gameRoomPasswordInput = QLineEdit(self.centralwidget)
        self.gameRoomPasswordInput.setObjectName(u"gameRoomPasswordInput")
        self.gameRoomPasswordInput.setGeometry(QRect(90, 150, 120, 20))
        self.gameRoomPasswordInput.setInputMethodHints(Qt.ImhDigitsOnly)
        self.gameRoomNameInput = QLineEdit(self.centralwidget)
        self.gameRoomNameInput.setObjectName(u"gameRoomNameInput")
        self.gameRoomNameInput.setGeometry(QRect(90, 120, 120, 20))
        self.playerName = QLineEdit(self.centralwidget)
        self.playerName.setObjectName(u"playerName")
        self.playerName.setGeometry(QRect(90, 180, 120, 20))
        self.worldInfoInput = QLineEdit(self.centralwidget)
        self.worldInfoInput.setObjectName(u"worldInfoInput")
        self.worldInfoInput.setGeometry(QRect(90, 210, 20, 20))
        self.worldInfoInput.setInputMethodHints(Qt.ImhDigitsOnly)
        self.connectionSelection = QComboBox(self.centralwidget)
        self.connectionSelection.addItem("")
        self.connectionSelection.addItem("")
        self.connectionSelection.setObjectName(u"connectionSelection")
        self.connectionSelection.setGeometry(QRect(90, 30, 120, 20))
        self.worldInfoLabel = QLabel(self.centralwidget)
        self.worldInfoLabel.setObjectName(u"worldInfoLabel")
        self.worldInfoLabel.setGeometry(QRect(9, 210, 71, 20))
        self.worldInfoLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gameRoomPasswordLabel = QLabel(self.centralwidget)
        self.gameRoomPasswordLabel.setObjectName(u"gameRoomPasswordLabel")
        self.gameRoomPasswordLabel.setGeometry(QRect(25, 150, 55, 16))
        self.gameRoomPasswordLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.playerNameLabel = QLabel(self.centralwidget)
        self.playerNameLabel.setObjectName(u"playerNameLabel")
        self.playerNameLabel.setGeometry(QRect(10, 180, 70, 20))
        self.playerNameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.serverIPLabel = QLabel(self.centralwidget)
        self.serverIPLabel.setObjectName(u"serverIPLabel")
        self.serverIPLabel.setGeometry(QRect(40, 90, 40, 20))
        self.serverIPLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gameRoomNameLabel = QLabel(self.centralwidget)
        self.gameRoomNameLabel.setObjectName(u"gameRoomNameLabel")
        self.gameRoomNameLabel.setGeometry(QRect(10, 120, 70, 20))
        self.gameRoomNameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.readyBox = QCheckBox(self.centralwidget)
        self.readyBox.setObjectName(u"readyBox")
        self.readyBox.setGeometry(QRect(220, 280, 90, 20))
        self.readyBox.setLayoutDirection(Qt.RightToLeft)
        self.joinButton = QPushButton(self.centralwidget)
        self.joinButton.setObjectName(u"joinButton")
        self.joinButton.setGeometry(QRect(90, 240, 75, 25))
        self.disconnectButton = QPushButton(self.centralwidget)
        self.disconnectButton.setObjectName(u"disconnectButton")
        self.disconnectButton.setGeometry(QRect(120, 280, 75, 25))
        self.modeSelector = QComboBox(self.centralwidget)
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.setObjectName(u"modeSelector")
        self.modeSelector.setGeometry(QRect(90, 60, 120, 20))
        self.gameModeSelectorLabel = QLabel(self.centralwidget)
        self.gameModeSelectorLabel.setObjectName(u"gameModeSelectorLabel")
        self.gameModeSelectorLabel.setGeometry(QRect(10, 60, 71, 16))
        self.gameModeSelectorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wind Waker Multiworld", None))
        self.serverButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.serverIpInput.setText("")
        self.gameRoomPasswordInput.setText("")
        self.connectionSelection.setItemText(0, QCoreApplication.translate("MainWindow", u"Connect to Room", None))
        self.connectionSelection.setItemText(1, QCoreApplication.translate("MainWindow", u"Create Room", None))

        self.worldInfoLabel.setText(QCoreApplication.translate("MainWindow", u"World ID", None))
        self.gameRoomPasswordLabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.playerNameLabel.setText(QCoreApplication.translate("MainWindow", u"Player Name", None))
        self.serverIPLabel.setText(QCoreApplication.translate("MainWindow", u"Server", None))
        self.gameRoomNameLabel.setText(QCoreApplication.translate("MainWindow", u"Room Name", None))
        self.readyBox.setText(QCoreApplication.translate("MainWindow", u" Ready to Play", None))
        self.joinButton.setText(QCoreApplication.translate("MainWindow", u"Join", None))
        self.disconnectButton.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.modeSelector.setItemText(0, QCoreApplication.translate("MainWindow", u"Multiworld", None))
        self.modeSelector.setItemText(1, QCoreApplication.translate("MainWindow", u"Coop", None))

        self.gameModeSelectorLabel.setText(QCoreApplication.translate("MainWindow", u"Game Mode", None))
    # retranslateUi

