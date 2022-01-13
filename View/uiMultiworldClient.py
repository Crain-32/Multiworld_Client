# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'multiworldClient.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class uiMultiworldClient(object):
    
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
        self.serverButton.setGeometry(QRect(20, 280, 75, 25))
        self.serverIpInput = QLineEdit(self.centralwidget)
        self.serverIpInput.setObjectName(u"serverIpInput")
        self.serverIpInput.setGeometry(QRect(80, 60, 120, 20))
        self.serverPortInput = QLineEdit(self.centralwidget)
        self.serverPortInput.setObjectName(u"serverPortInput")
        self.serverPortInput.setGeometry(QRect(80, 90, 60, 20))
        self.serverPortInput.setInputMethodHints(Qt.ImhDigitsOnly)
        self.gameRoomNameInput = QLineEdit(self.centralwidget)
        self.gameRoomNameInput.setObjectName(u"gameRoomNameInput")
        self.gameRoomNameInput.setGeometry(QRect(80, 120, 120, 20))
        self.playerName = QLineEdit(self.centralwidget)
        self.playerName.setObjectName(u"playerName")
        self.playerName.setGeometry(QRect(80, 210, 110, 20))
        self.worldIdInput = QLineEdit(self.centralwidget)
        self.worldIdInput.setObjectName(u"worldIdInput")
        self.worldIdInput.setGeometry(QRect(80, 240, 20, 20))
        self.worldIdInput.setInputMethodHints(Qt.ImhDigitsOnly)
        self.maxPlayersInput = QLineEdit(self.centralwidget)
        self.maxPlayersInput.setObjectName(u"maxPlayersInput")
        self.maxPlayersInput.setGeometry(QRect(80, 150, 20, 20))
        self.modeSelector = QComboBox(self.centralwidget)
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.setObjectName(u"modeSelector")
        self.modeSelector.setGeometry(QRect(20, 20, 120, 20))
        self.maxPLayersLabel = QLabel(self.centralwidget)
        self.maxPLayersLabel.setObjectName(u"maxPLayersLabel")
        self.maxPLayersLabel.setGeometry(QRect(8, 150, 70, 20))
        self.worldIdLabel = QLabel(self.centralwidget)
        self.worldIdLabel.setObjectName(u"worldIdLabel")
        self.worldIdLabel.setGeometry(QRect(27, 240, 50, 20))
        self.serverPortLabel = QLabel(self.centralwidget)
        self.serverPortLabel.setObjectName(u"serverPortLabel")
        self.serverPortLabel.setGeometry(QRect(17, 90, 60, 20))
        self.playerNameLabel = QLabel(self.centralwidget)
        self.playerNameLabel.setObjectName(u"playerNameLabel")
        self.playerNameLabel.setGeometry(QRect(7, 210, 70, 20))
        self.serverIPLabel = QLabel(self.centralwidget)
        self.serverIPLabel.setObjectName(u"serverIPLabel")
        self.serverIPLabel.setGeometry(QRect(27, 60, 50, 20))
        self.gameRoomNameLabel = QLabel(self.centralwidget)
        self.gameRoomNameLabel.setObjectName(u"gameRoomNameLabel")
        self.gameRoomNameLabel.setGeometry(QRect(8, 120, 70, 20))
        self.readyBox = QCheckBox(self.centralwidget)
        self.readyBox.setObjectName(u"readyBox")
        self.readyBox.setGeometry(QRect(200, 280, 90, 20))
        self.readyBox.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wind Waker Multiworld", None))
        self.serverButton.setText(QCoreApplication.translate("MainWindow", u"Set-Up", None))
        self.serverIpInput.setText("")
        self.serverPortInput.setText("")
        self.modeSelector.setItemText(0, QCoreApplication.translate("MainWindow", u"Connect to Room", None))
        self.modeSelector.setItemText(1, QCoreApplication.translate("MainWindow", u"Set-up Room", None))

        self.maxPLayersLabel.setText(QCoreApplication.translate("MainWindow", u"Max Players", None))
        self.worldIdLabel.setText(QCoreApplication.translate("MainWindow", u"World ID", None))
        self.serverPortLabel.setText(QCoreApplication.translate("MainWindow", u"Server Port", None))
        self.playerNameLabel.setText(QCoreApplication.translate("MainWindow", u"Player Name", None))
        self.serverIPLabel.setText(QCoreApplication.translate("MainWindow", u"Server IP", None))
        self.gameRoomNameLabel.setText(QCoreApplication.translate("MainWindow", u"Room Name", None))
        self.readyBox.setText(QCoreApplication.translate("MainWindow", u" Ready to Play", None))
    # retranslateUi

