# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_parameter_settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(491, 386)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lab_settings = QLabel(self.centralwidget)
        self.lab_settings.setObjectName(u"lab_settings")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_settings.sizePolicy().hasHeightForWidth())
        self.lab_settings.setSizePolicy(sizePolicy)
        self.lab_settings.setLayoutDirection(Qt.LeftToRight)
        self.lab_settings.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lab_settings)

        self.grid_parameter = QGridLayout()
        self.grid_parameter.setObjectName(u"grid_parameter")

        self.verticalLayout.addLayout(self.grid_parameter)

        self.btn_save_settings = QPushButton(self.centralwidget)
        self.btn_save_settings.setObjectName(u"btn_save_settings")

        self.verticalLayout.addWidget(self.btn_save_settings)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 7)
        self.verticalLayout.setStretch(2, 2)

        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lab_settings.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_save_settings.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
    # retranslateUi

