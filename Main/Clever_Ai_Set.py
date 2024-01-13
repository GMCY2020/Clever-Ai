# -*- coding: utf-8 -*-
# https://blog.csdn.net/weixin_46554689
# Created by: GMCY
# 2021/2/10

from os import path
from time import sleep
from sys import argv, exit
from threading import Thread
from PyQt5.QtGui import QStandardItem
from PyQt5 import QtCore, QtGui, QtWidgets
from socket import socket, AF_INET, SOCK_DGRAM


class UiSetWindow(object):
    def __init__(self):
        self.loc_model = None
        self.tableView_loc = None
        self.label_local_path = None
        self.pushButton_app_start = None
        self.app_model = None
        self.label_app_path = None
        self.lineEdit_self_keywords = None
        self.pushButton_self = None
        self.self_model = None
        self.label_self_path = None
        self.lineEdit_self_path = None
        self.pushButton_self_path_save = None
        self.widget_air = None
        self.pushButton_air = None
        self.label_tuling_URL = None
        self.label_tuling_ID = None
        self.lineEdit_tuling_ID = None
        self.lineEdit_tuling_KEY = None
        self.pushButton_air_load = None
        self.tableView_self = None
        self.label_self_keywords = None
        self.label_self_backWords = None
        self.pushButton_self_load = None
        self.textEdit_self_backWords = None
        self.widget_self = None
        self.lineEdit_app_name = None
        self.label_tuling_KEY = None
        self.lineEdit_tuling_URL = None
        self.buttons = None
        self.pushButton_local = None
        self.pushButton_local_path_save = None
        self.lineEdit_local_path = None
        self.widget_local = None
        self.pushButton_app = None
        self.pushButton_app_load = None
        self.label_app_name = None
        self.lineEdit_app_path = None
        self.widget_app = None
        self.lineEdit_user_name = None
        self.tableView_app = None
        self.pushButton_message_save = None
        self.lineEdit_robot_name = None
        self.label_robot_name = None
        self.label_user_name = None
        self.widget_message = None
        self.scrollAreaWidgetContents = None
        self.scrollArea = None
        self.centralWidget = None
        self.Messages = {}
        self.app_y = 0
        self.loc_y = 0
        self.self_y = 0

    def setupUi(self, SetWindow):
        SetWindow.setObjectName("SetWindow")
        SetWindow.resize(680, 550)
        SetWindow.setMinimumSize(QtCore.QSize(680, 550))
        SetWindow.setMaximumSize(QtCore.QSize(680, 550))
        self.centralWidget = QtWidgets.QWidget(SetWindow)
        self.centralWidget.setObjectName("central-widget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 681, 551))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -155, 658, 2248))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget_message = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_message.setGeometry(QtCore.QRect(0, 0, 661, 171))
        self.widget_message.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.widget_message.setObjectName("widget_message")
        self.label_user_name = QtWidgets.QLabel(self.widget_message)
        self.label_user_name.setGeometry(QtCore.QRect(20, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_user_name.setFont(font)
        self.label_user_name.setObjectName("label_user_name")
        self.label_robot_name = QtWidgets.QLabel(self.widget_message)
        self.label_robot_name.setGeometry(QtCore.QRect(20, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_robot_name.setFont(font)
        self.label_robot_name.setObjectName("label_robot_name")
        self.lineEdit_user_name = QtWidgets.QLineEdit(self.widget_message)
        self.lineEdit_user_name.setGeometry(QtCore.QRect(110, 30, 421, 31))
        self.lineEdit_user_name.setMinimumSize(QtCore.QSize(421, 31))
        self.lineEdit_user_name.setMaximumSize(QtCore.QSize(421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_user_name.setFont(font)
        self.lineEdit_user_name.setObjectName("lineEdit_user_name")
        self.lineEdit_robot_name = QtWidgets.QLineEdit(self.widget_message)
        self.lineEdit_robot_name.setGeometry(QtCore.QRect(110, 70, 421, 31))
        self.lineEdit_robot_name.setMinimumSize(QtCore.QSize(421, 31))
        self.lineEdit_robot_name.setMaximumSize(QtCore.QSize(421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_robot_name.setFont(font)
        self.lineEdit_robot_name.setObjectName("lineEdit_robot_name")
        self.pushButton_message_save = QtWidgets.QPushButton(self.widget_message)
        self.pushButton_message_save.setGeometry(QtCore.QRect(550, 120, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_message_save.setFont(font)
        self.pushButton_message_save.setStyleSheet("background-color: rgb(255, 255, 222);")
        self.pushButton_message_save.setObjectName("pushButton_message_save")
        self.widget_app = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_app.setGeometry(QtCore.QRect(0, 170, 661, 571))
        self.widget_app.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.widget_app.setObjectName("widget_app")
        self.tableView_app = QtWidgets.QTableView(self.widget_app)
        self.tableView_app.setGeometry(QtCore.QRect(130, 70, 511, 361))
        self.tableView_app.setMinimumSize(QtCore.QSize(511, 0))
        self.tableView_app.setMaximumSize(QtCore.QSize(511, 16777215))
        self.tableView_app.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableView_app.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView_app.setObjectName("tableView_app")

        self.app_model = QtGui.QStandardItemModel()
        self.tableView_app.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView_app.horizontalHeader().setVisible(False)
        self.tableView_app.verticalHeader().setVisible(False)
        app_font = QtGui.QFont()
        app_font.setPointSize(12)
        self.tableView_app.setFont(app_font)
        self.tableView_app.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.lineEdit_app_path = QtWidgets.QLineEdit(self.widget_app)
        self.lineEdit_app_path.setGeometry(QtCore.QRect(220, 490, 421, 31))
        self.lineEdit_app_path.setMinimumSize(QtCore.QSize(421, 31))
        self.lineEdit_app_path.setMaximumSize(QtCore.QSize(421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_app_path.setFont(font)
        self.lineEdit_app_path.setObjectName("lineEdit_app_path")
        self.lineEdit_app_name = QtWidgets.QLineEdit(self.widget_app)
        self.lineEdit_app_name.setGeometry(QtCore.QRect(220, 450, 421, 31))
        self.lineEdit_app_name.setMinimumSize(QtCore.QSize(421, 31))
        self.lineEdit_app_name.setMaximumSize(QtCore.QSize(421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_app_name.setFont(font)
        self.lineEdit_app_name.setObjectName("lineEdit_app_name")
        self.pushButton_app_load = QtWidgets.QPushButton(self.widget_app)
        self.pushButton_app_load.setGeometry(QtCore.QRect(550, 530, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_app_load.setFont(font)
        self.pushButton_app_load.setStyleSheet("background-color: rgb(255, 255, 222);")
        self.pushButton_app_load.setObjectName("pushButton_app_load")
        self.label_app_name = QtWidgets.QLabel(self.widget_app)
        self.label_app_name.setGeometry(QtCore.QRect(120, 450, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_app_name.setFont(font)
        self.label_app_name.setObjectName("label_app_name")
        self.label_app_path = QtWidgets.QLabel(self.widget_app)
        self.label_app_path.setGeometry(QtCore.QRect(120, 490, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_app_path.setFont(font)
        self.label_app_path.setObjectName("label_app_path")
        self.pushButton_app_start = QtWidgets.QPushButton(self.widget_app)
        self.pushButton_app_start.setGeometry(QtCore.QRect(130, 20, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_app_start.setFont(font)
        self.pushButton_app_start.setStyleSheet("background-color: rgb(255, 255, 222);")
        self.pushButton_app_start.setObjectName("pushButton_app_start")
        self.pushButton_app = QtWidgets.QPushButton(self.widget_app)
        self.pushButton_app.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_app.setFont(font)
        self.pushButton_app.setStyleSheet('""')
        self.pushButton_app.setObjectName("pushButton_app")
        self.widget_local = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_local.setGeometry(QtCore.QRect(0, 740, 661, 501))
        self.widget_local.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.widget_local.setObjectName("widget_local")
        self.lineEdit_local_path = QtWidgets.QLineEdit(self.widget_local)
        self.lineEdit_local_path.setGeometry(QtCore.QRect(220, 70, 321, 31))
        self.lineEdit_local_path.setMinimumSize(QtCore.QSize(0, 31))
        self.lineEdit_local_path.setMaximumSize(QtCore.QSize(421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_local_path.setFont(font)
        self.lineEdit_local_path.setText("")
        self.lineEdit_local_path.setObjectName("lineEdit_local_path")
        self.pushButton_local_path_save = QtWidgets.QPushButton(self.widget_local)
        self.pushButton_local_path_save.setGeometry(QtCore.QRect(550, 70, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_local_path_save.setFont(font)
        self.pushButton_local_path_save.setStyleSheet("background-color: rgb(255, 255, 222);")
        self.pushButton_local_path_save.setObjectName("pushButton_local_path_save")
        self.label_local_path = QtWidgets.QLabel(self.widget_local)
        self.label_local_path.setGeometry(QtCore.QRect(120, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_local_path.setFont(font)
        self.label_local_path.setObjectName("label_local_path")
        self.tableView_loc = QtWidgets.QTableView(self.widget_local)
        self.tableView_loc.setGeometry(QtCore.QRect(130, 120, 511, 361))
        self.tableView_loc.setMinimumSize(QtCore.QSize(511, 0))
        self.tableView_loc.setMaximumSize(QtCore.QSize(511, 16777215))
        self.tableView_loc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableView_loc.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView_loc.setObjectName("tableView_loc")

        self.loc_model = QtGui.QStandardItemModel()
        self.tableView_loc.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView_loc.horizontalHeader().setVisible(False)
        self.tableView_loc.verticalHeader().setVisible(False)
        loc_font = QtGui.QFont()
        loc_font.setPointSize(12)
        self.tableView_loc.setFont(loc_font)
        self.tableView_loc.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.pushButton_local = QtWidgets.QPushButton(self.widget_local)
        self.pushButton_local.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_local.setFont(font)
        self.pushButton_local.setStyleSheet('""')
        self.pushButton_local.setObjectName("pushButton_local")
        self.widget_self = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_self.setGeometry(QtCore.QRect(0, 1240, 661, 771))
        self.widget_self.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.widget_self.setObjectName("widget_self")
        self.textEdit_self_backWords = QtWidgets.QTextEdit(self.widget_self)
        self.textEdit_self_backWords.setGeometry(QtCore.QRect(220, 550, 421, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_self_backWords.setFont(font)
        self.textEdit_self_backWords.setObjectName("textEdit_self_backwards")
        self.pushButton_self_load = QtWidgets.QPushButton(self.widget_self)
        self.pushButton_self_load.setGeometry(QtCore.QRect(550, 720, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_self_load.setFont(font)
        self.pushButton_self_load.setStyleSheet("background-color: rgb(255, 255, 222);")
        self.pushButton_self_load.setObjectName("pushButton_self_load")
        self.label_self_backWords = QtWidgets.QLabel(self.widget_self)
        self.label_self_backWords.setGeometry(QtCore.QRect(130, 550, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_self_backWords.setFont(font)
        self.label_self_backWords.setObjectName("label_self_backwards")
        self.lineEdit_self_keywords = QtWidgets.QLineEdit(self.widget_self)
        self.lineEdit_self_keywords.setGeometry(QtCore.QRect(220, 500, 421, 31))
        self.lineEdit_self_keywords.setMinimumSize(QtCore.QSize(421, 31))
        self.lineEdit_self_keywords.setMaximumSize(QtCore.QSize(421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_self_keywords.setFont(font)
        self.lineEdit_self_keywords.setObjectName("lineEdit_self_keywords")
        self.label_self_keywords = QtWidgets.QLabel(self.widget_self)
        self.label_self_keywords.setGeometry(QtCore.QRect(130, 500, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_self_keywords.setFont(font)
        self.label_self_keywords.setObjectName("label_self_keywords")
        self.tableView_self = QtWidgets.QTableView(self.widget_self)
        self.tableView_self.setGeometry(QtCore.QRect(140, 130, 511, 361))
        self.tableView_self.setMinimumSize(QtCore.QSize(511, 0))
        self.tableView_self.setMaximumSize(QtCore.QSize(511, 16777215))
        self.tableView_self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableView_self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView_self.setObjectName("tableView_self")

        self.self_model = QtGui.QStandardItemModel()
        self.tableView_self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView_self.horizontalHeader().setVisible(False)
        self.tableView_self.verticalHeader().setVisible(False)
        self_font = QtGui.QFont()
        self_font.setPointSize(12)
        self.tableView_self.setFont(self_font)
        self.tableView_self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.pushButton_self = QtWidgets.QPushButton(self.widget_self)
        self.pushButton_self.setGeometry(QtCore.QRect(20, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_self.setFont(font)
        self.pushButton_self.setStyleSheet('""')
        self.pushButton_self.setObjectName("pushButton_self")
        self.label_self_path = QtWidgets.QLabel(self.widget_self)
        self.label_self_path.setGeometry(QtCore.QRect(130, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_self_path.setFont(font)
        self.label_self_path.setObjectName("label_self_path")
        self.pushButton_self_path_save = QtWidgets.QPushButton(self.widget_self)
        self.pushButton_self_path_save.setGeometry(QtCore.QRect(560, 80, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_self_path_save.setFont(font)
        self.pushButton_self_path_save.setStyleSheet("background-color: rgb(255, 255, 222);")
        self.pushButton_self_path_save.setObjectName("pushButton_self_path_save")
        self.lineEdit_self_path = QtWidgets.QLineEdit(self.widget_self)
        self.lineEdit_self_path.setGeometry(QtCore.QRect(230, 80, 321, 31))
        self.lineEdit_self_path.setMinimumSize(QtCore.QSize(0, 31))
        self.lineEdit_self_path.setMaximumSize(QtCore.QSize(421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_self_path.setFont(font)
        self.lineEdit_self_path.setText("")
        self.lineEdit_self_path.setObjectName("lineEdit_self_path")
        self.widget_air = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_air.setGeometry(QtCore.QRect(0, 2010, 661, 241))
        self.widget_air.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.widget_air.setObjectName("widget_air")
        self.label_tuling_URL = QtWidgets.QLabel(self.widget_air)
        self.label_tuling_URL.setGeometry(QtCore.QRect(130, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_tuling_URL.setFont(font)
        self.label_tuling_URL.setObjectName("label_tuling_URL")
        self.label_tuling_ID = QtWidgets.QLabel(self.widget_air)
        self.label_tuling_ID.setGeometry(QtCore.QRect(130, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_tuling_ID.setFont(font)
        self.label_tuling_ID.setObjectName("label_tuling_ID")
        self.lineEdit_tuling_ID = QtWidgets.QLineEdit(self.widget_air)
        self.lineEdit_tuling_ID.setGeometry(QtCore.QRect(220, 150, 421, 31))
        self.lineEdit_tuling_ID.setMinimumSize(QtCore.QSize(421, 31))
        self.lineEdit_tuling_ID.setMaximumSize(QtCore.QSize(421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_tuling_ID.setFont(font)
        self.lineEdit_tuling_ID.setText("")
        self.lineEdit_tuling_ID.setObjectName("lineEdit_tuling_ID")
        self.pushButton_air_load = QtWidgets.QPushButton(self.widget_air)
        self.pushButton_air_load.setGeometry(QtCore.QRect(550, 200, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_air_load.setFont(font)
        self.pushButton_air_load.setStyleSheet("background-color: rgb(255, 255, 222);")
        self.pushButton_air_load.setObjectName("pushButton_air_load")
        self.lineEdit_tuling_KEY = QtWidgets.QLineEdit(self.widget_air)
        self.lineEdit_tuling_KEY.setGeometry(QtCore.QRect(220, 110, 421, 31))
        self.lineEdit_tuling_KEY.setMinimumSize(QtCore.QSize(421, 31))
        self.lineEdit_tuling_KEY.setMaximumSize(QtCore.QSize(421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_tuling_KEY.setFont(font)
        self.lineEdit_tuling_KEY.setText("")
        self.lineEdit_tuling_KEY.setObjectName("lineEdit_tuling_KEY")
        self.label_tuling_KEY = QtWidgets.QLabel(self.widget_air)
        self.label_tuling_KEY.setGeometry(QtCore.QRect(130, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_tuling_KEY.setFont(font)
        self.label_tuling_KEY.setObjectName("label_tuling_KEY")
        self.lineEdit_tuling_URL = QtWidgets.QLineEdit(self.widget_air)
        self.lineEdit_tuling_URL.setGeometry(QtCore.QRect(220, 70, 421, 31))
        self.lineEdit_tuling_URL.setMinimumSize(QtCore.QSize(421, 31))
        self.lineEdit_tuling_URL.setMaximumSize(QtCore.QSize(421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_tuling_URL.setFont(font)
        self.lineEdit_tuling_URL.setText("")
        self.lineEdit_tuling_URL.setObjectName("lineEdit_tuling_URL")
        self.pushButton_air = QtWidgets.QPushButton(self.widget_air)
        self.pushButton_air.setGeometry(QtCore.QRect(20, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_air.setFont(font)
        self.pushButton_air.setStyleSheet('""')
        self.pushButton_air.setObjectName("pushButton_air")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        SetWindow.setCentralWidget(self.centralWidget)

        self.reTranslateUi(SetWindow)
        QtCore.QMetaObject.connectSlotsByName(SetWindow)

    def reTranslateUi(self, SetWindow):
        _translate = QtCore.QCoreApplication.translate
        SetWindow.setWindowTitle(_translate("SetWindow", "设置"))
        self.label_user_name.setText(_translate("SetWindow", "用户名："))
        self.label_robot_name.setText(_translate("SetWindow", "机器名："))
        self.lineEdit_user_name.setText(_translate("SetWindow", ""))
        self.lineEdit_robot_name.setText(_translate("SetWindow", ""))
        self.pushButton_message_save.setText(_translate("SetWindow", "保存"))
        self.lineEdit_app_path.setText(_translate("SetWindow", "应用的地址"))
        self.lineEdit_app_name.setText(_translate("SetWindow", "用空格分开"))
        self.pushButton_app_load.setText(_translate("SetWindow", "加载"))
        self.label_app_name.setText(_translate("SetWindow", "应用名："))
        self.label_app_path.setText(_translate("SetWindow", "应用地址："))
        self.pushButton_app_start.setText(_translate("SetWindow", "初始化"))
        self.pushButton_app.setText(_translate("SetWindow", "使用应用"))
        self.pushButton_local_path_save.setText(_translate("SetWindow", "保存"))
        self.label_local_path.setText(_translate("SetWindow", "词库地址："))
        self.pushButton_local.setText(_translate("SetWindow", "本地词库"))
        self.textEdit_self_backWords.setHtml(_translate("SetWindow",
                                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                        "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                        "<html><head><meta name=\"RichTextFX\" content=\"1\" /><style "
                                                        "type=\"text/css\">\n "
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:\'SimSun\'; "
                                                        "font-size:12pt; font-weight:400; font-style:normal;\">\n "
                                                        "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                        "text-indent:0px;\">语句1</p>\n "
                                                        "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                        "text-indent:0px;\">语句2</p>\n "
                                                        "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                        "text-indent:0px;\">语句3</p>\n "
                                                        "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                        "text-indent:0px;\">（每一行为一种答复）</p>\n "
                                                        "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                        "text-indent:0px;\">（[user]会替换为用户的名字）</p>\n "
                                                        "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                        "text-indent:0px;\">（[robot]会替换为机器人的名字）</p></body></html>"))
        self.pushButton_self_load.setText(_translate("SetWindow", "加载"))
        self.label_self_backWords.setText(_translate("SetWindow", "答复语句："))
        self.lineEdit_self_keywords.setText(_translate("SetWindow", "用空格分开"))
        self.label_self_keywords.setText(_translate("SetWindow", "关键词句："))
        self.pushButton_self.setText(_translate("SetWindow", "自定义词库"))
        self.label_self_path.setText(_translate("SetWindow", "词库地址："))
        self.pushButton_self_path_save.setText(_translate("SetWindow", "保存"))
        self.label_tuling_URL.setText(_translate("SetWindow", "API_URL:"))
        self.label_tuling_ID.setText(_translate("SetWindow", "USER_ID:"))
        self.pushButton_air_load.setText(_translate("SetWindow", "加载"))
        self.label_tuling_KEY.setText(_translate("SetWindow", "API_KEY:"))
        self.pushButton_air.setText(_translate("SetWindow", "云机器人"))

        self.pushButton()

    def pushButton(self):
        self.pushButton_message_save.clicked.connect(self.message_save)
        self.pushButton_app.clicked.connect(self.app)
        self.pushButton_app_start.clicked.connect(self.app_start)
        self.pushButton_app_load.clicked.connect(self.app_load)
        self.pushButton_local.clicked.connect(self.local)
        self.pushButton_local_path_save.clicked.connect(self.local_path_save)
        self.pushButton_self.clicked.connect(self.my_self)
        self.pushButton_self_load.clicked.connect(self.self_load)
        self.pushButton_self_path_save.clicked.connect(self.self_path_save)
        self.pushButton_air.clicked.connect(self.air)
        self.pushButton_air_load.clicked.connect(self.air_load)

        self.get_messages()
        self.fresh_button()
        self.Fresh()
        self.fresh_set_line_message()

    def message_save(self):
        String_dict = self.Messages
        String_dict['command'] = 're_messages'
        String_dict['robot_name'] = self.lineEdit_robot_name.text()
        String_dict['user_name'] = self.lineEdit_user_name.text()
        self.ClientServer(String_dict)

    def set_button(self, num):
        if self.buttons[num] == '1':
            self.buttons[num] = '0'
        else:
            self.buttons[num] = '1'

        self.re_message()
        self.fresh_button()

    def app(self):
        self.set_button(1)

    def app_start(self):
        thread_app = Thread(target=self.fresh_set_app_message)
        thread_app.start()

    def app_load(self):
        appNames = self.lineEdit_app_name.text()
        apppath = self.lineEdit_app_path.text()
        app_path = '..\\Messages\\0_app_messages.txt'
        with open(app_path, 'a', encoding='utf-8') as f:
            f.write(appNames + '\n')
            f.write(apppath + '\n')
            f.write('\n')

        self.lineEdit_app_name.setText("用空格分开")
        self.lineEdit_app_path.setText("应用的地址")

        thread_app = Thread(target=self.fresh_set_app_message)
        thread_app.start()

    def local(self):
        self.set_button(2)

    def local_path_save(self):
        String_dict = self.Messages
        String_dict['command'] = 're_messages'
        String_dict['local_path'] = self.lineEdit_local_path.text()
        self.ClientServer(String_dict)

        sleep(1)

        thread_loc = Thread(target=self.fresh_set_local_message)
        thread_loc.start()

    def my_self(self):
        self.set_button(3)

    def self_load(self):
        keyWorks = self.lineEdit_self_keywords.text()
        backWorks = self.textEdit_self_backWords.toPlainText()
        self_path = self.Messages['self_path']
        with open(self_path, 'a', encoding='utf-8') as f:
            f.write(keyWorks + '\n')
            f.write(backWorks + '\n')
            f.write('\n')

        self.lineEdit_self_keywords.setText("用空格分开")
        self.textEdit_self_backWords.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"RichTextFX\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; "
            "font-style:normal;\">\n "
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
            "text-indent:0px;\">语句1</p>\n "
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
            "text-indent:0px;\">语句2</p>\n "
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
            "text-indent:0px;\">语句3</p>\n "
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
            "text-indent:0px;\">（每一行为一种答复）</p>\n "
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
            "text-indent:0px;\">（[user]会替换为用户的名字）</p>\n "
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
            "text-indent:0px;\">（[robot]会替换为机器人的名字）</p></body></html>")

        thread_self = Thread(target=self.fresh_set_self_message)
        thread_self.start()

    def self_path_save(self):
        String_dict = self.Messages
        String_dict['command'] = 're_messages'
        String_dict['self_path'] = self.lineEdit_self_path.text()
        self.ClientServer(String_dict)

        sleep(1)

        thread_self = Thread(target=self.fresh_set_self_message)
        thread_self.start()

    def air(self):
        self.set_button(4)

    def air_load(self):
        String_dict = self.Messages
        String_dict['command'] = 're_messages'
        String_dict['tuling_URL'] = self.lineEdit_tuling_URL.text()
        String_dict['tuling_KEY'] = self.lineEdit_tuling_KEY.text()
        String_dict['tuling_ID'] = self.lineEdit_tuling_ID.text()
        self.ClientServer(String_dict)

    def ClientServer(self, String_dict):
        client = socket(AF_INET, SOCK_DGRAM)
        msg = str(String_dict).strip().encode('utf-8')
        client.sendto(msg, ('127.0.0.1', 9000))
        back, addr = client.recvfrom(1024)
        self.Messages = eval(back.decode('utf-8'))

    def get_messages(self):
        String_dict = self.Messages
        String_dict['command'] = 'get_messages'
        self.ClientServer(String_dict)
        self.buttons = self.Messages['buttons']

    def re_message(self):
        String_dict = self.Messages
        String_dict['command'] = 're_messages'
        String_dict['buttons'] = self.buttons
        self.ClientServer(String_dict)

    def fresh_button(self):
        if self.buttons[1] == '0' and self.pushButton_app.styleSheet() == "background-color: rgb(85, 255, 127);":
            self.pushButton_app.setStyleSheet("background-color: rgb(255, 85, 0);")
        elif self.buttons[1] == '1' and self.pushButton_app.styleSheet() == "background-color: rgb(255, 85, 0);":
            self.pushButton_app.setStyleSheet("background-color: rgb(85, 255, 127);")
        elif self.buttons[1] == '0' and self.pushButton_app.styleSheet() == '""':
            self.pushButton_app.setStyleSheet("background-color: rgb(255, 85, 0);")
        elif self.buttons[1] == '1' and self.pushButton_app.styleSheet() == '""':
            self.pushButton_app.setStyleSheet("background-color: rgb(85, 255, 127);")
        else:
            pass

        if self.buttons[2] == '0' and self.pushButton_local.styleSheet() == "background-color: rgb(85, 255, 127);":
            self.pushButton_local.setStyleSheet("background-color: rgb(255, 85, 0);")
        elif self.buttons[2] == '1' and self.pushButton_local.styleSheet() == "background-color: rgb(255, 85, 0);":
            self.pushButton_local.setStyleSheet("background-color: rgb(85, 255, 127);")
        elif self.buttons[2] == '0' and self.pushButton_local.styleSheet() == '""':
            self.pushButton_local.setStyleSheet("background-color: rgb(255, 85, 0);")
        elif self.buttons[2] == '1' and self.pushButton_local.styleSheet() == '""':
            self.pushButton_local.setStyleSheet("background-color: rgb(85, 255, 127);")
        else:
            pass

        if self.buttons[3] == '0' and self.pushButton_self.styleSheet() == "background-color: rgb(85, 255, 127);":
            self.pushButton_self.setStyleSheet("background-color: rgb(255, 85, 0);")
        elif self.buttons[3] == '1' and self.pushButton_self.styleSheet() == "background-color: rgb(255, 85, 0);":
            self.pushButton_self.setStyleSheet("background-color: rgb(85, 255, 127);")
        elif self.buttons[3] == '0' and self.pushButton_self.styleSheet() == '""':
            self.pushButton_self.setStyleSheet("background-color: rgb(255, 85, 0);")
        elif self.buttons[3] == '1' and self.pushButton_self.styleSheet() == '""':
            self.pushButton_self.setStyleSheet("background-color: rgb(85, 255, 127);")
        else:
            pass

        if self.buttons[4] == '0' and self.pushButton_air.styleSheet() == "background-color: rgb(85, 255, 127);":
            self.pushButton_air.setStyleSheet("background-color: rgb(255, 85, 0);")
        elif self.buttons[4] == '1' and self.pushButton_air.styleSheet() == "background-color: rgb(255, 85, 0);":
            self.pushButton_air.setStyleSheet("background-color: rgb(85, 255, 127);")
        elif self.buttons[4] == '0' and self.pushButton_air.styleSheet() == '""':
            self.pushButton_air.setStyleSheet("background-color: rgb(255, 85, 0);")
        elif self.buttons[4] == '1' and self.pushButton_air.styleSheet() == '""':
            self.pushButton_air.setStyleSheet("background-color: rgb(85, 255, 127);")
        else:
            pass

    def fresh_set(self):
        num = 1
        while True:
            try:
                self.get_messages()
                self.fresh_button()
                sleep(0.1)

            except:
                break
            num += 1
            if self.Messages['command'] == 'exit' and num >= 25:
                app = QtWidgets.QApplication.instance()
                app.quit()
                break

    def fresh_set_line_message(self):
        self.lineEdit_user_name.setText(self.Messages['user_name'])
        self.lineEdit_robot_name.setText(self.Messages['robot_name'])
        self.lineEdit_local_path.setText(self.Messages['local_path'])
        self.lineEdit_self_path.setText(self.Messages['self_path'])
        self.lineEdit_tuling_URL.setText(self.Messages['tuling_URL'])
        self.lineEdit_tuling_KEY.setText(self.Messages['tuling_KEY'])
        self.lineEdit_tuling_ID.setText(self.Messages['tuling_ID'])

    def fresh_set_app_message(self):
        self.app_model.clear()
        sleep(0.1)
        self.app_y = 0

        app_path = '..\\Messages\\0_app_messages.txt'
        with open(app_path, 'r', encoding='utf-8') as f:
            self.tableView_app.clearMask()
            String = f.readlines()
            for Str in String:
                message = Str.split('\n')[0]
                self.display_app(message)

    def fresh_set_local_message(self):
        self.loc_model.clear()
        sleep(0.1)
        self.loc_y = 0

        local_path = self.Messages['local_path']
        path_TF = path.exists(local_path)
        try:
            if path_TF:
                with open(local_path, 'r', encoding='utf-8') as f_local:
                    String_local = f_local.readlines()
                    for i in range(200):
                        self.display_loc(String_local[i].split('\n')[0])

                self.display_loc('')
                self.display_loc('注意: 为保证其稳定,默认加载前200条语句!!!')
            else:
                self.display_loc('没有该文件，请输入正确文件地址!!!')
        except:
            pass

    def fresh_set_self_message(self):
        self.self_model.clear()
        sleep(0.1)
        self.self_y = 0

        self_path = self.Messages['self_path']
        path_TF = path.exists(self_path)
        if path_TF:
            with open(self_path, 'r', encoding='utf-8') as f_self:
                String_self = f_self.readlines()
                for Str_self in String_self:
                    self.display_self(Str_self.split('\n')[0])
        else:
            self.display_self('没有该文件，请输入正确文件地址!!!')

    def display_app(self, String):
        app_item = QStandardItem(String)
        self.app_model.setItem(self.app_y, 0, app_item)
        self.tableView_app.setModel(self.app_model)
        sleep(0.01)
        self.tableView_app.scrollToBottom()
        self.app_y += 1

    def display_loc(self, String):
        loc_item = QStandardItem(String)
        self.loc_model.setItem(self.loc_y, 0, loc_item)
        self.tableView_loc.setModel(self.loc_model)
        sleep(0.00001)
        self.tableView_loc.scrollToBottom()
        self.loc_y += 1

    def display_self(self, String):
        self_item = QStandardItem(String)
        self.self_model.setItem(self.self_y, 0, self_item)
        self.tableView_self.setModel(self.self_model)
        sleep(0.01)
        self.tableView_self.scrollToBottom()
        self.self_y += 1

    def Fresh(self):
        thread = Thread(target=self.fresh_set)
        thread.start()

        thread_app = Thread(target=self.fresh_set_app_message)
        thread_app.start()

        thread_loc = Thread(target=self.fresh_set_local_message)
        thread_loc.start()

        thread_self = Thread(target=self.fresh_set_self_message)
        thread_self.start()


def show_SetWindow():
    App = QtWidgets.QApplication(argv)
    App.setWindowIcon(QtGui.QIcon('Ai_Set.ico'))
    MainWindow = QtWidgets.QMainWindow()
    ui = UiSetWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    exit(App.exec_())


if __name__ == '__main__':
    show_SetWindow()
