# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(996, 646)
        MainWindow.setMinimumSize(QSize(800, 550))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toodle = QFrame(self.frame_top)
        self.frame_toodle.setObjectName(u"frame_toodle")
        self.frame_toodle.setMinimumSize(QSize(80, 55))
        self.frame_toodle.setMaximumSize(QSize(80, 55))
        self.frame_toodle.setStyleSheet(u"background:rgb(0,143,150);")
        self.frame_toodle.setFrameShape(QFrame.NoFrame)
        self.frame_toodle.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toodle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toodle = QPushButton(self.frame_toodle)
        self.toodle.setObjectName(u"toodle")
        self.toodle.setMinimumSize(QSize(80, 55))
        self.toodle.setMaximumSize(QSize(80, 55))
        self.toodle.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,178,178);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../../../../.designer/backup/images/AITAD_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toodle.setIcon(icon)
        self.toodle.setIconSize(QSize(22, 20))
        self.toodle.setFlat(True)

        self.horizontalLayout_3.addWidget(self.toodle)


        self.horizontalLayout.addWidget(self.frame_toodle)

        self.frame_top_east = QFrame(self.frame_top)
        self.frame_top_east.setObjectName(u"frame_top_east")
        self.frame_top_east.setMaximumSize(QSize(16777215, 55))
        self.frame_top_east.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_top_east.setFrameShape(QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.topbar_name = QFrame(self.frame_top_east)
        self.topbar_name.setObjectName(u"topbar_name")
        self.topbar_name.setFrameShape(QFrame.NoFrame)
        self.topbar_name.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.topbar_name)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lab_appname = QLabel(self.topbar_name)
        self.lab_appname.setObjectName(u"lab_appname")
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        font.setPointSize(24)
        self.lab_appname.setFont(font)
        self.lab_appname.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_10.addWidget(self.lab_appname)


        self.horizontalLayout_4.addWidget(self.topbar_name)

        self.topbar_part_2 = QFrame(self.frame_top_east)
        self.topbar_part_2.setObjectName(u"topbar_part_2")
        self.topbar_part_2.setFrameShape(QFrame.NoFrame)
        self.topbar_part_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.topbar_part_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lab_user = QLabel(self.topbar_part_2)
        self.lab_user.setObjectName(u"lab_user")
        self.lab_user.setFont(font)
        self.lab_user.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_user.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lab_user)


        self.horizontalLayout_4.addWidget(self.topbar_part_2)

        self.topbar_settings = QFrame(self.frame_top_east)
        self.topbar_settings.setObjectName(u"topbar_settings")
        self.topbar_settings.setMinimumSize(QSize(55, 55))
        self.topbar_settings.setMaximumSize(QSize(55, 55))
        self.topbar_settings.setFrameShape(QFrame.NoFrame)
        self.topbar_settings.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.topbar_settings)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.bn_settings = QPushButton(self.topbar_settings)
        self.bn_settings.setObjectName(u"bn_settings")
        self.bn_settings.setMaximumSize(QSize(55, 55))
        self.bn_settings.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(0,0,0,0);\n"
"}")

        self.horizontalLayout_8.addWidget(self.bn_settings)


        self.horizontalLayout_4.addWidget(self.topbar_settings)

        self.topbar_min = QFrame(self.frame_top_east)
        self.topbar_min.setObjectName(u"topbar_min")
        self.topbar_min.setMinimumSize(QSize(55, 55))
        self.topbar_min.setMaximumSize(QSize(55, 55))
        self.topbar_min.setFrameShape(QFrame.NoFrame)
        self.topbar_min.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.topbar_min)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bn_min = QPushButton(self.topbar_min)
        self.bn_min.setObjectName(u"bn_min")
        self.bn_min.setMaximumSize(QSize(55, 55))
        self.bn_min.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../../../../../.designer/backup/images/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_min.setIcon(icon1)
        self.bn_min.setIconSize(QSize(22, 22))
        self.bn_min.setFlat(True)

        self.horizontalLayout_7.addWidget(self.bn_min)


        self.horizontalLayout_4.addWidget(self.topbar_min)

        self.topbar_max = QFrame(self.frame_top_east)
        self.topbar_max.setObjectName(u"topbar_max")
        self.topbar_max.setMinimumSize(QSize(55, 55))
        self.topbar_max.setMaximumSize(QSize(55, 55))
        self.topbar_max.setFrameShape(QFrame.NoFrame)
        self.topbar_max.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.topbar_max)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bn_max = QPushButton(self.topbar_max)
        self.bn_max.setObjectName(u"bn_max")
        self.bn_max.setMaximumSize(QSize(55, 55))
        self.bn_max.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../../../../../.designer/backup/images/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_max.setIcon(icon2)
        self.bn_max.setIconSize(QSize(22, 22))
        self.bn_max.setFlat(True)

        self.horizontalLayout_6.addWidget(self.bn_max)


        self.horizontalLayout_4.addWidget(self.topbar_max)

        self.topbar_close = QFrame(self.frame_top_east)
        self.topbar_close.setObjectName(u"topbar_close")
        self.topbar_close.setMinimumSize(QSize(55, 55))
        self.topbar_close.setMaximumSize(QSize(55, 55))
        self.topbar_close.setFrameShape(QFrame.NoFrame)
        self.topbar_close.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.topbar_close)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bn_close = QPushButton(self.topbar_close)
        self.bn_close.setObjectName(u"bn_close")
        self.bn_close.setMaximumSize(QSize(55, 55))
        self.bn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../../../../../../.designer/backup/images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_close.setIcon(icon3)
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setFlat(True)

        self.horizontalLayout_5.addWidget(self.bn_close)


        self.horizontalLayout_4.addWidget(self.topbar_close)


        self.horizontalLayout.addWidget(self.frame_top_east)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_west = QFrame(self.frame_bottom)
        self.frame_bottom_west.setObjectName(u"frame_bottom_west")
        self.frame_bottom_west.setMinimumSize(QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QSize(80, 16777215))
        self.frame_bottom_west.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_bottom_west.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.frame_bottom_west)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setMinimumSize(QSize(80, 55))
        self.frame_main.setMaximumSize(QSize(160, 55))
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_main)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bn_navi_main = QPushButton(self.frame_main)
        self.bn_navi_main.setObjectName(u"bn_navi_main")
        self.bn_navi_main.setMinimumSize(QSize(80, 55))
        self.bn_navi_main.setMaximumSize(QSize(160, 55))
        self.bn_navi_main.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../../../../../../.designer/backup/images/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_navi_main.setIcon(icon4)
        self.bn_navi_main.setIconSize(QSize(22, 22))
        self.bn_navi_main.setFlat(True)

        self.horizontalLayout_15.addWidget(self.bn_navi_main)


        self.verticalLayout_3.addWidget(self.frame_main)

        self.frame_cut = QFrame(self.frame_bottom_west)
        self.frame_cut.setObjectName(u"frame_cut")
        self.frame_cut.setMinimumSize(QSize(80, 55))
        self.frame_cut.setMaximumSize(QSize(160, 55))
        self.frame_cut.setFrameShape(QFrame.NoFrame)
        self.frame_cut.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_cut)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.bn_navi_cut = QPushButton(self.frame_cut)
        self.bn_navi_cut.setObjectName(u"bn_navi_cut")
        self.bn_navi_cut.setMinimumSize(QSize(80, 55))
        self.bn_navi_cut.setMaximumSize(QSize(160, 55))
        self.bn_navi_cut.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../../../../../../.designer/backup/images/plan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_navi_cut.setIcon(icon5)
        self.bn_navi_cut.setIconSize(QSize(22, 22))
        self.bn_navi_cut.setFlat(True)

        self.horizontalLayout_16.addWidget(self.bn_navi_cut)


        self.verticalLayout_3.addWidget(self.frame_cut)

        self.frame_vis = QFrame(self.frame_bottom_west)
        self.frame_vis.setObjectName(u"frame_vis")
        self.frame_vis.setMinimumSize(QSize(80, 55))
        self.frame_vis.setMaximumSize(QSize(160, 55))
        self.frame_vis.setFrameShape(QFrame.NoFrame)
        self.frame_vis.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_vis)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.bn_navi_vis = QPushButton(self.frame_vis)
        self.bn_navi_vis.setObjectName(u"bn_navi_vis")
        self.bn_navi_vis.setMinimumSize(QSize(80, 55))
        self.bn_navi_vis.setMaximumSize(QSize(160, 55))
        self.bn_navi_vis.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../../../../../../.designer/backup/images/Recording.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_navi_vis.setIcon(icon6)
        self.bn_navi_vis.setIconSize(QSize(22, 12))
        self.bn_navi_vis.setFlat(True)

        self.horizontalLayout_17.addWidget(self.bn_navi_vis)


        self.verticalLayout_3.addWidget(self.frame_vis)

        self.frame_spacer = QFrame(self.frame_bottom_west)
        self.frame_spacer.setObjectName(u"frame_spacer")
        self.frame_spacer.setFrameShape(QFrame.NoFrame)
        self.frame_spacer.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_spacer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_spacer)


        self.horizontalLayout_2.addWidget(self.frame_bottom_west)

        self.frame_bottom_east = QFrame(self.frame_bottom)
        self.frame_bottom_east.setObjectName(u"frame_bottom_east")
        self.frame_bottom_east.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_bottom_east)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 55))
        self.stackedWidget.setStyleSheet(u"")
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.page_main.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_19 = QHBoxLayout(self.page_main)
        self.horizontalLayout_19.setSpacing(20)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.lay_main_left = QVBoxLayout()
        self.lay_main_left.setObjectName(u"lay_main_left")
        self.lay_main_left.setContentsMargins(20, 20, 20, 20)
        self.label_5 = QLabel(self.page_main)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_5.setFont(font1)

        self.lay_main_left.addWidget(self.label_5)

        self.widget = QWebEngineView(self.page_main)
        self.widget.setObjectName(u"widget")

        self.lay_main_left.addWidget(self.widget)

        self.lay_main_left.setStretch(0, 2)
        self.lay_main_left.setStretch(1, 20)

        self.horizontalLayout_19.addLayout(self.lay_main_left)

        self.lay_main_right = QVBoxLayout()
        self.lay_main_right.setSpacing(20)
        self.lay_main_right.setObjectName(u"lay_main_right")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.lab_import = QLabel(self.page_main)
        self.lab_import.setObjectName(u"lab_import")
        self.lab_import.setFont(font1)

        self.verticalLayout_10.addWidget(self.lab_import)

        self.list_import = QListWidget(self.page_main)
        self.list_import.setObjectName(u"list_import")

        self.verticalLayout_10.addWidget(self.list_import)

        self.btn_import = QPushButton(self.page_main)
        self.btn_import.setObjectName(u"btn_import")

        self.verticalLayout_10.addWidget(self.btn_import)

        self.verticalLayout_10.setStretch(0, 2)
        self.verticalLayout_10.setStretch(1, 20)
        self.verticalLayout_10.setStretch(2, 2)

        self.lay_main_right.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.lab_export = QLabel(self.page_main)
        self.lab_export.setObjectName(u"lab_export")
        self.lab_export.setFont(font1)

        self.verticalLayout_11.addWidget(self.lab_export)

        self.list_saved = QListWidget(self.page_main)
        self.list_saved.setObjectName(u"list_saved")

        self.verticalLayout_11.addWidget(self.list_saved)

        self.btn_export = QPushButton(self.page_main)
        self.btn_export.setObjectName(u"btn_export")

        self.verticalLayout_11.addWidget(self.btn_export)


        self.lay_main_right.addLayout(self.verticalLayout_11)

        self.lay_main_right.setStretch(0, 1)
        self.lay_main_right.setStretch(1, 1)

        self.horizontalLayout_19.addLayout(self.lay_main_right)

        self.horizontalLayout_19.setStretch(0, 20)
        self.horizontalLayout_19.setStretch(1, 10)
        self.stackedWidget.addWidget(self.page_main)
        self.page_about_main = QWidget()
        self.page_about_main.setObjectName(u"page_about_main")
        self.page_about_main.setStyleSheet(u"background:rgb(91,90,90);")
        self.gridLayout_3 = QGridLayout(self.page_about_main)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lab_about_main = QLabel(self.page_about_main)
        self.lab_about_main.setObjectName(u"lab_about_main")
        self.lab_about_main.setMinimumSize(QSize(0, 55))
        self.lab_about_main.setMaximumSize(QSize(16777215, 55))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(24)
        self.lab_about_main.setFont(font2)
        self.lab_about_main.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_3.addWidget(self.lab_about_main, 0, 0, 1, 1)

        self.frame_about_main = QFrame(self.page_about_main)
        self.frame_about_main.setObjectName(u"frame_about_main")
        self.frame_about_main.setFrameShape(QFrame.StyledPanel)
        self.frame_about_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_about_main)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 5, 0, 5)
        self.text_about_main = QTextEdit(self.frame_about_main)
        self.text_about_main.setObjectName(u"text_about_main")
        self.text_about_main.setEnabled(True)
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.text_about_main.setFont(font3)
        self.text_about_main.setStyleSheet(u"color:rgb(255,255,255);")
        self.text_about_main.setFrameShape(QFrame.NoFrame)
        self.text_about_main.setFrameShadow(QFrame.Plain)
        self.text_about_main.setReadOnly(True)
        self.text_about_main.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.horizontalLayout_28.addWidget(self.text_about_main)

        self.scroll_about_main = QScrollBar(self.frame_about_main)
        self.scroll_about_main.setObjectName(u"scroll_about_main")
        self.scroll_about_main.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.scroll_about_main.setOrientation(Qt.Vertical)

        self.horizontalLayout_28.addWidget(self.scroll_about_main)


        self.gridLayout_3.addWidget(self.frame_about_main, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_about_main)
        self.page_about_cutting = QWidget()
        self.page_about_cutting.setObjectName(u"page_about_cutting")
        self.page_about_cutting.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_29 = QHBoxLayout(self.page_about_cutting)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lab_about_cutting = QLabel(self.page_about_cutting)
        self.lab_about_cutting.setObjectName(u"lab_about_cutting")
        self.lab_about_cutting.setFont(font1)

        self.verticalLayout_5.addWidget(self.lab_about_cutting)

        self.text_about_cutting = QTextEdit(self.page_about_cutting)
        self.text_about_cutting.setObjectName(u"text_about_cutting")

        self.verticalLayout_5.addWidget(self.text_about_cutting)


        self.horizontalLayout_29.addLayout(self.verticalLayout_5)

        self.stackedWidget.addWidget(self.page_about_cutting)
        self.rtst = QWidget()
        self.rtst.setObjectName(u"rtst")
        self.rtst.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.rtst)
        self.page_vis = QWidget()
        self.page_vis.setObjectName(u"page_vis")
        self.page_vis.setStyleSheet(u"background:rgb(91,90,90);")
        self.gridLayout = QGridLayout(self.page_vis)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textBrowser_plan = QTextBrowser(self.page_vis)
        self.textBrowser_plan.setObjectName(u"textBrowser_plan")

        self.gridLayout.addWidget(self.textBrowser_plan, 3, 0, 1, 1)

        self.top_frame_plan = QHBoxLayout()
        self.top_frame_plan.setObjectName(u"top_frame_plan")
        self.top_frame_plan.setContentsMargins(-1, 10, -1, 10)
        self.lab_plan = QLabel(self.page_vis)
        self.lab_plan.setObjectName(u"lab_plan")
        self.lab_plan.setFont(font1)

        self.top_frame_plan.addWidget(self.lab_plan)


        self.gridLayout.addLayout(self.top_frame_plan, 2, 0, 1, 1)

        self.verticalScrollBar_plan = QScrollBar(self.page_vis)
        self.verticalScrollBar_plan.setObjectName(u"verticalScrollBar_plan")
        self.verticalScrollBar_plan.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.verticalScrollBar_plan, 3, 1, 1, 1)

        self.horizontalSlider_plan = QSlider(self.page_vis)
        self.horizontalSlider_plan.setObjectName(u"horizontalSlider_plan")
        self.horizontalSlider_plan.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_plan, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_vis)
        self.page_about_vis = QWidget()
        self.page_about_vis.setObjectName(u"page_about_vis")
        self.page_about_vis.setStyleSheet(u"background:rgb(91,90,90);")
        self.gridLayout_4 = QGridLayout(self.page_about_vis)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.lab_plan_2 = QLabel(self.page_about_vis)
        self.lab_plan_2.setObjectName(u"lab_plan_2")
        self.lab_plan_2.setMinimumSize(QSize(0, 55))
        self.lab_plan_2.setMaximumSize(QSize(16777215, 55))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semilight")
        font4.setPointSize(24)
        self.lab_plan_2.setFont(font4)
        self.lab_plan_2.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.lab_plan_2, 0, 0, 1, 1)

        self.textEdit_plan = QTextEdit(self.page_about_vis)
        self.textEdit_plan.setObjectName(u"textEdit_plan")

        self.gridLayout_4.addWidget(self.textEdit_plan, 1, 0, 1, 1)

        self.verticalScrollBar = QScrollBar(self.page_about_vis)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.verticalScrollBar, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_about_vis)
        self.page_cutting = QWidget()
        self.page_cutting.setObjectName(u"page_cutting")
        self.page_cutting.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_8 = QVBoxLayout(self.page_cutting)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.lab_recording_main = QLabel(self.page_cutting)
        self.lab_recording_main.setObjectName(u"lab_recording_main")
        self.lab_recording_main.setMinimumSize(QSize(0, 55))
        self.lab_recording_main.setMaximumSize(QSize(16777215, 55))
        self.lab_recording_main.setFont(font2)
        self.lab_recording_main.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_8.addWidget(self.lab_recording_main)

        self.frame_2 = QFrame(self.page_cutting)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setMinimumSize(QSize(0, 235))
        self.frame_2.setMaximumSize(QSize(16777215, 235))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        self.frame_2.setFont(font5)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(14)
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.line_label4 = QLineEdit(self.frame_2)
        self.line_label4.setObjectName(u"line_label4")
        self.line_label4.setMinimumSize(QSize(400, 25))
        self.line_label4.setMaximumSize(QSize(500, 25))
        self.line_label4.setFont(font5)
        self.line_label4.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.line_label4, 2, 1, 1, 3)

        self.line_label2 = QLineEdit(self.frame_2)
        self.line_label2.setObjectName(u"line_label2")
        self.line_label2.setEnabled(True)
        self.line_label2.setMinimumSize(QSize(400, 25))
        self.line_label2.setMaximumSize(QSize(500, 25))
        self.line_label2.setFont(font5)
        self.line_label2.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.line_label2, 0, 1, 1, 3)

        self.line_label3 = QLineEdit(self.frame_2)
        self.line_label3.setObjectName(u"line_label3")
        self.line_label3.setMinimumSize(QSize(400, 25))
        self.line_label3.setMaximumSize(QSize(500, 25))
        self.line_label3.setFont(font5)
        self.line_label3.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.line_label3, 1, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 3, 0, 1, 2)

        self.bn_recording_start = QPushButton(self.frame_2)
        self.bn_recording_start.setObjectName(u"bn_recording_start")
        self.bn_recording_start.setEnabled(True)
        self.bn_recording_start.setMinimumSize(QSize(69, 25))
        self.bn_recording_start.setMaximumSize(QSize(69, 25))
        self.bn_recording_start.setFont(font5)
        self.bn_recording_start.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.bn_recording_start, 3, 2, 1, 1)

        self.bn_recording_connect = QPushButton(self.frame_2)
        self.bn_recording_connect.setObjectName(u"bn_recording_connect")
        self.bn_recording_connect.setMinimumSize(QSize(69, 25))
        self.bn_recording_connect.setMaximumSize(QSize(69, 25))
        self.bn_recording_connect.setFont(font5)
        self.bn_recording_connect.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.bn_recording_connect, 3, 3, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 162, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_cutting)
        self.rtst_2 = QWidget()
        self.rtst_2.setObjectName(u"rtst_2")
        self.rtst_2.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_9 = QVBoxLayout(self.rtst_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.rtst_2)

        self.horizontalLayout_14.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_low = QFrame(self.frame_bottom_east)
        self.frame_low.setObjectName(u"frame_low")
        self.frame_low.setMinimumSize(QSize(0, 20))
        self.frame_low.setMaximumSize(QSize(16777215, 20))
        self.frame_low.setStyleSheet(u"")
        self.frame_low.setFrameShape(QFrame.NoFrame)
        self.frame_low.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_tab = QFrame(self.frame_low)
        self.frame_tab.setObjectName(u"frame_tab")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        self.frame_tab.setFont(font7)
        self.frame_tab.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_tab.setFrameShape(QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lab_tab = QLabel(self.frame_tab)
        self.lab_tab.setObjectName(u"lab_tab")
        font8 = QFont()
        font8.setFamily(u"Segoe UI Light")
        font8.setPointSize(10)
        self.lab_tab.setFont(font8)
        self.lab_tab.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_12.addWidget(self.lab_tab)


        self.horizontalLayout_11.addWidget(self.frame_tab)

        self.frame_drag = QFrame(self.frame_low)
        self.frame_drag.setObjectName(u"frame_drag")
        self.frame_drag.setMinimumSize(QSize(20, 20))
        self.frame_drag.setMaximumSize(QSize(20, 20))
        self.frame_drag.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_drag.setFrameShape(QFrame.NoFrame)
        self.frame_drag.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.frame_drag)


        self.verticalLayout_2.addWidget(self.frame_low)


        self.horizontalLayout_2.addWidget(self.frame_bottom_east)


        self.verticalLayout.addWidget(self.frame_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toodle.setText("")
        self.lab_appname.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lab_user.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Seiten\u00fcberschrift</p><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.bn_settings.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.bn_settings.setText("")
#if QT_CONFIG(tooltip)
        self.bn_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_min.setText("")
#if QT_CONFIG(tooltip)
        self.bn_max.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_max.setText("")
#if QT_CONFIG(tooltip)
        self.bn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.bn_close.setText("")
#if QT_CONFIG(tooltip)
        self.bn_navi_main.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.bn_navi_main.setText("")
#if QT_CONFIG(tooltip)
        self.bn_navi_cut.setToolTip(QCoreApplication.translate("MainWindow", u"Bug", None))
#endif // QT_CONFIG(tooltip)
        self.bn_navi_cut.setText("")
#if QT_CONFIG(tooltip)
        self.bn_navi_vis.setToolTip(QCoreApplication.translate("MainWindow", u"Cloud", None))
#endif // QT_CONFIG(tooltip)
        self.bn_navi_vis.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Visualisierung aller Daten", None))
        self.lab_import.setText(QCoreApplication.translate("MainWindow", u"Liste aller Importierten Datein", None))
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"Importieren von Dateien", None))
        self.lab_export.setText(QCoreApplication.translate("MainWindow", u"Liste aller gespeicherten Prozessen", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"Exportieren von Dateien", None))
        self.lab_about_main.setText(QCoreApplication.translate("MainWindow", u"About: Main-Seite", None))
        self.text_about_main.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">Test text, hier wird alles Erkl\u00e4rt wie die spezifische Seite funktioniert</span></p></body></html>", None))
        self.lab_about_cutting.setText(QCoreApplication.translate("MainWindow", u"About: Schneiden", None))
        self.text_about_cutting.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:36pt;\">Test text, hier wird alles Erkl\u00e4rt wie die spezifische Seite funktioniert</span></p></body></html>", None))
        self.lab_plan.setText(QCoreApplication.translate("MainWindow", u"Visualisierung", None))
        self.lab_plan_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">About: Visualisierung</span></p></body></html>", None))
        self.textEdit_plan.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:36pt;\">Test text, hier wird alles Erkl\u00e4rt wie die spezifische Seite funktioniert</span></p></body></html>", None))
        self.lab_recording_main.setText(QCoreApplication.translate("MainWindow", u"Schneiden von Daten", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Startpunkt", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Endpunkt", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Interval", None))
        self.bn_recording_start.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.bn_recording_connect.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.lab_tab.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.frame_drag.setToolTip(QCoreApplication.translate("MainWindow", u"Drag", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

