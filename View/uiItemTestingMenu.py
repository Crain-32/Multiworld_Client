# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'itemTestingMenu.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class uiItemTestingMenu(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 450)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.itemSelection = QListWidget(self.centralwidget)
        self.itemSelection.setObjectName(u"itemSelection")
        self.itemSelection.setGeometry(QRect(30, 30, 201, 381))
        self.fromIdInput = QLineEdit(self.centralwidget)
        self.fromIdInput.setObjectName(u"fromIdInput")
        self.fromIdInput.setGeometry(QRect(290, 50, 113, 21))
        self.sendToServer = QPushButton(self.centralwidget)
        self.sendToServer.setObjectName(u"sendToServer")
        self.sendToServer.setGeometry(QRect(294, 340, 91, 24))
        self.sendToMe = QPushButton(self.centralwidget)
        self.sendToMe.setObjectName(u"sendToMe")
        self.sendToMe.setGeometry(QRect(310, 80, 75, 24))
        self.toIdInput = QLineEdit(self.centralwidget)
        self.toIdInput.setObjectName(u"toIdInput")
        self.toIdInput.setGeometry(QRect(290, 310, 113, 21))
        self.fromIdLabel = QLabel(self.centralwidget)
        self.fromIdLabel.setObjectName(u"fromIdLabel")
        self.fromIdLabel.setGeometry(QRect(240, 50, 49, 16))
        self.toIdLabel = QLabel(self.centralwidget)
        self.toIdLabel.setObjectName(u"toIdLabel")
        self.toIdLabel.setGeometry(QRect(250, 310, 49, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Item Testing Menu", None))
        self.sendToServer.setText(QCoreApplication.translate("MainWindow", u"Send to Them", None))
        self.sendToMe.setText(QCoreApplication.translate("MainWindow", u"Send to Me", None))
        self.fromIdLabel.setText(QCoreApplication.translate("MainWindow", u"From ID", None))
        self.toIdLabel.setText(QCoreApplication.translate("MainWindow", u"To ID", None))
    # retranslateUi

