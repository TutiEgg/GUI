# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_settings.ui'
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
        MainWindow.resize(363, 395)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, -1, 4, -1)
        self.lab_selected_list = QLabel(self.centralwidget)
        self.lab_selected_list.setObjectName(u"lab_selected_list")
        font = QFont()
        font.setPointSize(15)
        self.lab_selected_list.setFont(font)
        self.lab_selected_list.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lab_selected_list)

        self.list_selected = QListWidget(self.centralwidget)
        self.list_selected.setObjectName(u"list_selected")

        self.verticalLayout.addWidget(self.list_selected)

        self.list_selected_reset = QPushButton(self.centralwidget)
        self.list_selected_reset.setObjectName(u"list_selected_reset")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_selected_reset.sizePolicy().hasHeightForWidth())
        self.list_selected_reset.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.list_selected_reset.setFont(font1)

        self.verticalLayout.addWidget(self.list_selected_reset)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 11)
        self.verticalLayout.setStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, -1, 4, -1)
        self.lab_data_processing = QLabel(self.centralwidget)
        self.lab_data_processing.setObjectName(u"lab_data_processing")
        self.lab_data_processing.setFont(font1)

        self.verticalLayout_3.addWidget(self.lab_data_processing)

        self.list_data_processing = QListWidget(self.centralwidget)
        self.list_data_processing.setObjectName(u"list_data_processing")

        self.verticalLayout_3.addWidget(self.list_data_processing)

        self.lab_data_transformation = QLabel(self.centralwidget)
        self.lab_data_transformation.setObjectName(u"lab_data_transformation")
        self.lab_data_transformation.setFont(font1)

        self.verticalLayout_3.addWidget(self.lab_data_transformation)

        self.list_data_transformation = QListView(self.centralwidget)
        self.list_data_transformation.setObjectName(u"list_data_transformation")

        self.verticalLayout_3.addWidget(self.list_data_transformation)

        self.btn_settings_start = QPushButton(self.centralwidget)
        self.btn_settings_start.setObjectName(u"btn_settings_start")
        sizePolicy.setHeightForWidth(self.btn_settings_start.sizePolicy().hasHeightForWidth())
        self.btn_settings_start.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(20)
        self.btn_settings_start.setFont(font2)

        self.verticalLayout_3.addWidget(self.btn_settings_start)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 5)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 5)
        self.verticalLayout_3.setStretch(4, 2)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lab_selected_list.setText(QCoreApplication.translate("MainWindow", u"Ausgew\u00e4hlte Operationen", None))
        self.list_selected_reset.setText(QCoreApplication.translate("MainWindow", u"Reset Liste", None))
        self.lab_data_processing.setText(QCoreApplication.translate("MainWindow", u"Dataprocessing Funktionen", None))
        self.lab_data_transformation.setText(QCoreApplication.translate("MainWindow", u"Transformations Funktionen", None))
        self.btn_settings_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

