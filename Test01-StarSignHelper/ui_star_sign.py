# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'star-sign.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_NickName = QLineEdit(self.groupBox)
        self.lineEdit_NickName.setObjectName(u"lineEdit_NickName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_NickName)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_BirthDay = QLineEdit(self.groupBox)
        self.lineEdit_BirthDay.setObjectName(u"lineEdit_BirthDay")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_BirthDay)


        self.verticalLayout.addLayout(self.formLayout)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_Output = QGroupBox(self.centralwidget)
        self.groupBox_Output.setObjectName(u"groupBox_Output")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_Output)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.vbox = QVBoxLayout()
        self.vbox.setObjectName(u"vbox")

        self.verticalLayout_3.addLayout(self.vbox)


        self.verticalLayout_2.addWidget(self.groupBox_Output)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"User Input", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Your NickName:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Your Birthday:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Set OK", None))
        self.groupBox_Output.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
    # retranslateUi

