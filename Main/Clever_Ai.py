# -*- coding: utf-8 -*-
# https://blog.csdn.net/weixin_46554689
# Created by: GMCY
# 2021/2/10

from sys import argv, exit
from socket import socket, AF_INET, SOCK_DGRAM
from time import sleep, localtime
from threading import Thread
from PIL import ImageGrab
from random import choice
from win32con import CF_UNICODETEXT
from os import system, path
from json import dumps
from requests import post
from pyautogui import center, click, moveTo, hotkey, locateOnScreen, press, sleep
from win32clipboard import OpenClipboard, EmptyClipboard, SetClipboardData, CloseClipboard
from PyQt5 import QtCore, QtGui, QtWidgets
from aip import AipSpeech
from speech_recognition import Recognizer, Microphone
from win32com import client

speaker = client.Dispatch('SAPI.SpVoice')
speaker.Speak("", 0)


def my_Speak(String):
    try:
        speaker.Speak(str(String))
    except:
        with Microphone(sample_rate=16000) as source:
            print(source)
            pass
        speaker.Speak(str(String))


def my_record(rate=16000):
    r = Recognizer()
    with Microphone(sample_rate=rate) as source:
        audio = r.listen(source)

    with open('../Messages/voice.wav', 'wb') as f:
        f.write(audio.get_wav_data())


# 百度语音识别的 api, 在百度官网注册获取
API_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipSpeech(API_ID, API_KEY, SECRET_KEY)


def listen():
    if API_ID == '' or API_KEY == '' or SECRET_KEY == '':
        return "请先添加百度语音识别的Api"

    voice_path = '../Messages/voice.wav'
    with open(voice_path, 'rb') as fp:
        voices = fp.read()
    try:
        result = client.asr(voices, 'wav', 16000, {'dev_pid': 8002, })
        result_t = result['result'][0]
        for i in ['?', '？', ';', '.', '，', '。', ':', '/', '!', '！']:
            if i in result_t:
                result_t = result_t.split(i)
        result_text = ''
        for res in result_t:
            result_text += res
        return result_text
    except:
        return '我没有听清楚，请再说一遍。'


def ask_tuling(Tuling_API_URL, Tuling_API_KEY, Tuling_USER_ID, String):
    back = [None, 0]
    tuling_post_data = {"reqType": 0, "perception": {"inputText": {"text": String}}, "userInfo": {
        "apiKey": Tuling_API_KEY,
        "userId": Tuling_USER_ID
    }}
    json_data = dumps(tuling_post_data).encode('utf8')
    try:
        resp = post(url=Tuling_API_URL, headers={'content-type': 'application/json'}, data=json_data)
        if resp.status_code == 200:
            r = resp.json()
            if r:
                back = [r["results"][0]["values"]["text"], 1]
    except:
        back = '请在设置填入正确的数据!!!'
    return back


def history_write(String):
    times = localtime()
    daytime = str(times[0]) + '-' + str(times[1]) + '-' + str(times[2]) + '\t' + str(times[3]) + ':' + str(
        times[4]) + ':' + str(times[5])
    with open('..\\Messages\\history.txt', 'a', encoding='utf-8') as f:
        f.write(daytime + '\t\t' + String + '\n')


def StrSplit(String):
    Strings = []
    for i in String:
        Strings.append(i)

    String_lt = ['']
    Strs = ['']

    for S in Strings:
        for i in Strs:
            String_lt.append(i + S)
        Strs = []
        for j in String_lt:
            Strs.append(j)
    String_lt.remove('')
    String_lt.sort(key=lambda l: len(l), reverse=True)

    return String_lt


class MySplit:
    pass


def mouse_set_text(String):
    OpenClipboard()
    EmptyClipboard()
    SetClipboardData(CF_UNICODETEXT, String)
    CloseClipboard()


class Mouse:
    def __init__(self):
        self.pos_lt = []

    def mouse_pos(self, png):
        pos = locateOnScreen(png)
        if pos:
            self.pos_lt.append(pos)

    def mouse_xy(self, png_lt):
        error_xy = 0
        back_xy = None
        self.pos_lt.clear()
        threads = []

        for png in png_lt:
            path_png = '..\\Png\\%s' % png
            thread = Thread(
                target=self.mouse_pos,
                args=(path_png,)
            )
            thread.start()
            threads.append(thread)

        while threads:
            threads.pop().join()
            if len(self.pos_lt) != 0:
                error_xy = 1
                back_xy = self.pos_lt[0]
                break

        Lt = [back_xy, error_xy]

        return Lt

    def mouse_press(self, png_lt):
        error_press = 0
        xy, error_xy = self.mouse_xy(png_lt)
        if error_xy == 1:
            x, y = center(xy)
            moveTo(x, y)
            click(button='left')
            moveTo(960, 540)
            error_press = 1
        return error_press

    def mouse_search(self, png_lt, String):
        error_search = 0
        xy, error_xy = self.mouse_xy(png_lt)
        if error_xy == 1:
            for s in ['搜索一下', '搜索下', '搜索', '搜', '查找一下', '查找下', '查一下', '查下', '查', '翻译一下',
                      '翻译下', '翻译']:
                if s in String:
                    String = String.split(s)[1]
                    mouse_set_text(String=String)
            x, y = center(xy)
            moveTo(x, y)
            click(button='left')
            press('psp')
            hotkey('ctrl', 'a')
            press('psp')
            hotkey('ctrl', 'v')
            press('enter')
            moveTo(960, 540)
            error_search = 1
        return error_search


def ai_robot_local_MatchHeight(path_talk, String_lt):
    Back = ''
    error_matchHeight = 0

    with open(path_talk, 'r', encoding='utf-8') as f:
        while error_matchHeight == 0:
            keywords = f.readline().split('\n')[0].split(' ')
            backs = []
            back = f.readline().split('\n')[0]
            while back != '':
                backs.append(back)
                back = f.readline().split('\n')[0]

            for String in String_lt:
                for keyword in keywords:
                    if String == keyword:
                        error_matchHeight = 1
                        Back = choice(backs)
                        break
            if keywords == '' or backs == []:
                break
    lt_mh = [Back, error_matchHeight]
    return lt_mh


def ai_robot_local_MatchSimple(path_talk, String):
    Back = ''
    error_matchSplit = 0

    with open(path_talk, 'r', encoding='utf-8') as f:
        while error_matchSplit == 0:
            keywords = f.readline().split('\n')[0].split(' ')
            backs = []
            back = f.readline().split('\n')[0]
            while back != '':
                backs.append(back)
                back = f.readline().split('\n')[0]

            for keyword in keywords:
                if String == keyword:
                    error_matchSplit = 1
                    Back = choice(backs)
                    break
            if keywords == '' or backs == []:
                break
    lt_ms = [Back, error_matchSplit]
    return lt_ms


def ai_robot_local(path_talk, String):
    String_lt = StrSplit(String=String)
    a = ai_robot_local_MatchSimple(path_talk=path_talk, String=String)
    back = a[0]
    error_match = a[1]
    if error_match == 0:
        a = ai_robot_local_MatchHeight(path_talk=path_talk, String_lt=String_lt)
        back = a[0]
        error_match = a[1]
    Lt = [back, error_match]
    return Lt


class Talk:
    pass


def app_on_off(command):
    system(command)


class App:
    def __init__(self):
        self.M = Mouse()

    def app_main(self, path_app, String):
        error_app = 0
        back = None
        app_way = {
            'on': ['打开', '开', '登录一下', '登陆一下', '登录', '登陆', '登', '使用', '用', '听一下', '听', '想'],
            'off': ['关闭', '关', '退一下', '退出', '退', '结束'],
            'search': ['搜索', '搜索一下', '查找一下', '查找', '查', '找', '搜', '翻译一下', '翻译下', '翻译'],
            'normal': ['正常化', '正常'],
            'min': ['迷你化', '迷你', '最小化'],
            'right': ['下一首', '下首', '另一首'],
            'left': ['上一首', '上首'],
            'run': ['播放', '播', '放'],
            'stop': ['暂停', '停', '停止'],
        }

        Way = None
        error_way = 0
        for ways in app_way:
            for way in app_way[ways]:
                if way in String:
                    Way = ways
                    error_way = 1

        with open(path_app, 'r', encoding='utf-8') as f:
            error = 1
            while error == 1:
                appNames = f.readline().split('\n')[0].split(' ')
                on = f.readline().split('\n')[0]
                off = "%s" % (appNames[0].replace('-', ' ') + '.exe').lower()
                f.readline()

                if appNames == ['']:
                    if error_way == 1:
                        back = '未加载该应用'
                        error_app = 1
                    break

                for appname in appNames:
                    if appname in String or appname == String:
                        error = 0

                        if error_way == 1 and error_app == 0:
                            if Way == 'left' or Way == 'right' or Way == 'stop' or Way == 'run' or Way == 'min' or \
                                    Way == 'normal':
                                Png = '%s_%s_' % (appNames[0], Way)
                                Png_lt = [Png + '%s.png' % str(i) for i in range(1, 4)]
                                path_TF = path.exists('..\\Png\\%s' % Png_lt[0])
                                if path_TF:
                                    error_app = self.M.mouse_press(Png_lt)
                                    if error_app == 1:
                                        back = app_way[Way][0] + appNames[0] + '成功'
                                    else:
                                        error_app = 1
                                        back = app_way[Way][0] + appNames[0] + '失败'
                                else:
                                    error_app = 11
                                    back = Png_lt

                                history_write(Way + ':' + Png)

                            elif Way == 'search':
                                Png = '%s_%s_' % (appNames[0], Way)
                                Png_lt = [Png + '%s.png' % str(i) for i in range(1, 4)]
                                path_TF = path.exists('..\\Png\\%s' % Png_lt[0])
                                if path_TF:
                                    error_app = self.M.mouse_search(Png_lt, String)
                                    if error_app == 1:
                                        back = appNames[0] + app_way[Way][0] + '成功'
                                    else:
                                        back = appNames[0] + app_way[Way][0] + '失败'
                                else:
                                    error_app = 11
                                    back = Png_lt

                                history_write(Way + ':' + Png + ',' + String)

                            elif Way == 'off':
                                command = r'taskkill /f /t /im %s' % off
                                thread = Thread(
                                    target=app_on_off,
                                    args=(command,)
                                )
                                thread.start()
                                error_app = 1
                                back = app_way[Way][0] + appNames[0] + '成功'

                                history_write(Way + ':' + off)

                            elif Way == 'on':
                                command = r'"%s"' % on
                                thread = Thread(
                                    target=app_on_off,
                                    args=(command,)
                                )
                                thread.start()
                                error_app = 1
                                back = app_way[Way][0] + appNames[0] + '成功'

                                history_write(Way + ':' + on)
                        elif error_way == 0:
                            back = '请具体要使用' + appNames[0] + '的什么功能'
                            error_app = 1
                        else:
                            pass

        Lt = [back, error_app]
        return Lt


lock_set = 0


class UiMainWindow(object):
    def __init__(self):
        self.model = None
        self.user_name = None
        self.tuling_URL = None
        self.tuling_ID = None
        self.tuling_KEY = None
        self.buttons = None
        self.local_path = None
        self.Messages = None
        self.robot_name = None
        self.tableView = None
        self.pushButton_send_voice = None
        self.pushButton_send = None
        self.textEdit = None
        self.widget_send = None
        self.widget = None
        self.pushButton_air = None
        self.pushButton_self = None
        self.pushButton_local = None
        self.pushButton_app = None
        self.pushButton_voice = None
        self.pushButton_set = None
        self.widget_set = None
        self.centralWidget = None
        self.y = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 600)
        MainWindow.setMinimumSize(QtCore.QSize(860, 600))
        MainWindow.setMaximumSize(QtCore.QSize(860, 600))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setMinimumSize(QtCore.QSize(860, 600))
        self.centralWidget.setMaximumSize(QtCore.QSize(860, 600))
        self.centralWidget.setObjectName("central-widget")
        self.widget_set = QtWidgets.QWidget(self.centralWidget)
        self.widget_set.setGeometry(QtCore.QRect(0, 0, 171, 601))
        self.widget_set.setStyleSheet("background-color: rgb(237, 234, 233);")
        self.widget_set.setObjectName("widget_set")
        self.pushButton_set = QtWidgets.QPushButton(self.widget_set)
        self.pushButton_set.setGeometry(QtCore.QRect(30, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_set.setFont(font)
        self.pushButton_set.setStyleSheet("background-color: rgb(94, 94, 94);")
        self.pushButton_set.setObjectName("pushButton_set")
        self.pushButton_voice = QtWidgets.QPushButton(self.widget_set)
        self.pushButton_voice.setGeometry(QtCore.QRect(30, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_voice.setFont(font)
        self.pushButton_voice.setStyleSheet('""')
        self.pushButton_voice.setObjectName("pushButton_voice")
        self.pushButton_app = QtWidgets.QPushButton(self.widget_set)
        self.pushButton_app.setGeometry(QtCore.QRect(30, 140, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_app.setFont(font)
        self.pushButton_app.setStyleSheet('""')
        self.pushButton_app.setObjectName("pushButton_app")
        self.pushButton_local = QtWidgets.QPushButton(self.widget_set)
        self.pushButton_local.setGeometry(QtCore.QRect(30, 210, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_local.setFont(font)
        self.pushButton_local.setStyleSheet('""')
        self.pushButton_local.setObjectName("pushButton_local")
        self.pushButton_self = QtWidgets.QPushButton(self.widget_set)
        self.pushButton_self.setGeometry(QtCore.QRect(30, 280, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_self.setFont(font)
        self.pushButton_self.setStyleSheet('""')
        self.pushButton_self.setObjectName("pushButton_self")
        self.pushButton_air = QtWidgets.QPushButton(self.widget_set)
        self.pushButton_air.setGeometry(QtCore.QRect(30, 350, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_air.setFont(font)
        self.pushButton_air.setStyleSheet('""')
        self.pushButton_air.setObjectName("pushButton_air")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(170, 0, 691, 601))
        self.widget.setObjectName("widget")
        self.widget_send = QtWidgets.QWidget(self.widget)
        self.widget_send.setGeometry(QtCore.QRect(-1, 450, 691, 151))
        self.widget_send.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_send.setObjectName("widget_send")
        self.textEdit = QtWidgets.QTextEdit(self.widget_send)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 541, 151))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_send = QtWidgets.QPushButton(self.widget_send)
        self.pushButton_send.setGeometry(QtCore.QRect(560, 90, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_send.setFont(font)
        self.pushButton_send.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton_send.setObjectName("pushButton_send")
        self.pushButton_send_voice = QtWidgets.QPushButton(self.widget_send)
        self.pushButton_send_voice.setGeometry(QtCore.QRect(560, 30, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_send_voice.setFont(font)
        self.pushButton_send_voice.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton_send_voice.setObjectName("pushButton_send_voice")
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 691, 451))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableView.setFont(font)
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView.setObjectName("tableView")

        self.model = QtGui.QStandardItemModel()
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableView.setFont(font)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        MainWindow.setCentralWidget(self.centralWidget)

        self.reTranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def reTranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "智慧助手"))
        self.pushButton_set.setText(_translate("MainWindow", "设置"))
        self.pushButton_voice.setText(_translate("MainWindow", "语音回复"))
        self.pushButton_app.setText(_translate("MainWindow", "使用应用"))
        self.pushButton_local.setText(_translate("MainWindow", "本地词库"))
        self.pushButton_self.setText(_translate("MainWindow", "自定义库"))
        self.pushButton_air.setText(_translate("MainWindow", "云机器人"))
        self.pushButton_send.setText(_translate("MainWindow", "发送"))
        self.pushButton_send_voice.setText(_translate("MainWindow", "语音输入"))

        self.pushButton()
        self.get_messages()
        self.first_open()
        self.re_messages()
        self.fresh_button()

    def pushButton(self):
        self.pushButton_set.clicked.connect(self.Set)
        self.pushButton_voice.clicked.connect(self.voice)
        self.pushButton_app.clicked.connect(self.app)
        self.pushButton_local.clicked.connect(self.local)
        self.pushButton_self.clicked.connect(self.local_self)
        self.pushButton_air.clicked.connect(self.air)
        self.pushButton_send.clicked.connect(self.send_thread)
        self.pushButton_send_voice.clicked.connect(self.send_voice_thread)

    def Set(self):
        global lock_set
        if lock_set == 0:
            thread_Set_speak = Thread(target=self.Set_speak)
            thread_Set_speak.start()

        thread_show_set = Thread(target=show_SetWindow)
        thread_show_set.start()

        thread_FUWU = Thread(target=self.Server)
        thread_FUWU.start()

    def Set_speak(self):
        history_write('on:' + '设置')
        self.displayTable('', '设置已打开', 1)
        self.displayTable('', '若设置界面未正常加载请重新启动智慧助手', 1)

    def set_button(self, num):
        if self.buttons[num] == '1':
            self.buttons[num] = '0'
        else:
            self.buttons[num] = '1'
        self.re_messages()
        self.Fresh()

    def voice(self):
        self.set_button(0)

    def app(self):
        self.set_button(1)

    def local(self):
        self.set_button(2)

    def local_self(self):
        self.set_button(3)

    def air(self):
        self.set_button(4)

    def send_thread(self):
        if self.buttons[5] == '1':
            String = self.textEdit.toPlainText()
            if String != '':
                self.displayTable(self.user_name, String)
                thread = Thread(
                    target=self.ROBOT,
                    args=(String,)
                )
                thread.start()
                self.textEdit.clear()

    def send_voice_thread(self):
        thread = Thread(target=self.send_voice)
        thread.start()

    def send_voice(self):

        if self.buttons[5] == '1':

            self.buttons[5] = '0'
            self.re_messages()
            self.Fresh()

            self.displayTable('', '进入语音对话模式')

            my_record()
            String = listen()

            while String != 'EXIT' and String != 'exit' and String != 'Exit' and String != '结束程序' and \
                    String != '结束' and String != '退出' and String != '退出程序' and String != '结束一下程序' and \
                    String != '结束程序吧' and String != '关闭' and String != '关闭程序' and String != '关闭程序吧' and \
                    String != '结束对话' and String != "请先添加百度语音识别的Api":
                self.displayTable(self.user_name, String)
                self.ROBOT(String=String)
                my_record()
                String = listen()

            if String == '请先添加百度语音识别的Api':
                self.displayTable('', String)

            self.buttons[5] = '1'
            self.re_messages()
            self.Fresh()

            self.displayTable('', '退出语音对话模式')

    def ROBOT(self, String):
        back = None
        show = 0
        if '清空' in String and '屏幕' in String:
            self.y = 0
            self.model.clear()
            show = 1
        elif '打开' in String and '设置' in String:
            self.Set()
            show = 1
        elif ('关闭' in String or '退出' in String) and '设置' in String:
            self.Messages['command'] = 'exit'
            sleep(1)
            self.Messages['command'] = ''
            show = 1
        elif ('关闭' in String or '退出' in String) and '智慧助手' in String:
            app = QtWidgets.QApplication.instance()
            app.quit()
        elif '打开0_app_messages' in String or '打开应用信息' in String:
            thread = Thread(
                target=system,
                args=('..\\Messages\\0_app_messages.txt',)
            )
            thread.start()
            history_write('on' + ':' + '0_appmessages.txt')
            self.displayTable('', '打开应用信息成功')
            show = 1
        elif '打开0_talk' in String or '打开自定义词库' in String:
            thread = Thread(
                target=system,
                args=('..\\Messages\\talk.txt',)
            )
            thread.start()
            history_write('on' + ':' + 'talk.txt')
            self.displayTable('', '打开自定义词库成功')
            show = 1
        elif '打开history' in String or '打开历史记录' in String:
            thread = Thread(
                target=system,
                args=('..\\Messages\\history.txt',)
            )
            thread.start()
            history_write('on' + ':' + 'history.txt')
            self.displayTable('', '打开历史记录成功')
            show = 1

        if self.buttons[1] == '1' and show == 0:
            back = App().app_main(
                path_app='..\\Messages\\0_app_messages.txt',
                String=String
            )
            show = back[1]
        if self.buttons[3] == '1' and show == 0:
            back = ai_robot_local(
                path_talk=self.local_path[1],
                String=String
            )
            show = back[1]
        if self.buttons[2] == '1' and show == 0:
            back = ai_robot_local(
                path_talk=self.local_path[0],
                String=String
            )
            show = back[1]
        if self.buttons[4] == '1' and show == 0:
            back = ask_tuling(
                Tuling_API_URL=self.tuling_URL,
                Tuling_API_KEY=self.tuling_KEY,
                Tuling_USER_ID=self.tuling_ID,
                String=String
            )
            show = back[1]
        if show == 11:
            self.mouse_add_png(back[0])
        elif show == 1 and back is not None:
            self.displayTable('', back[0])
        elif show == 0 and \
                (self.buttons == ['0', '0', '0', '0', '0', '1'] or self.buttons == ['1', '0', '0', '0', '0', '1']):
            self.displayTable('', '请开起至少一个功能。')
        elif show == 0:
            self.displayTable('', '功能没有匹配的，可以打开云机器人。')

    def mouse_add_png(self, png_lt):
        self.displayTable('', '第一次使用该功能，请先手动截图。')
        for Png in png_lt:
            png = '..\\Png\\%s' % Png
            self.displayTable('图片加载', png, 1)
            self.displayTable('图片加载', '请截取按键或要点击的地方的图片', 1)
            hotkey('win', 'shift', 's')
            sleep(5)
            image = ImageGrab.grabclipboard()
            sleep(1)
            try:
                image.save('%s' % png)
                self.displayTable('图片加载', '%s加载成功' % png, 1)
            except:
                self.displayTable('图片加载', '%s加载失败' % png, 1)
        self.displayTable('', '截取完毕，可以正常使用该功能。')

    def get_messages(self):
        with open('..\\Messages\\0_messages.txt', 'r', encoding='utf-8') as f:
            self.robot_name = f.readline().split('\n')[0].split(':')[1]
            self.user_name = f.readline().split('\n')[0].split(':')[1]
            self.tuling_URL = f.readline().split('\n')[0].split('*')[1]
            self.tuling_KEY = f.readline().split('\n')[0].split(':')[1]
            self.tuling_ID = f.readline().split('\n')[0].split(':')[1]
            self.buttons = f.readline().split('\n')[0].split(':')[1].split('.')
            self.local_path = f.readline().split('\n')[0].split(':')[1].split('*')
            self.Messages = {
                'robot_name': self.robot_name,
                'user_name': self.user_name,
                'tuling_URL': self.tuling_URL,
                'tuling_KEY': self.tuling_KEY,
                'tuling_ID': self.tuling_ID,
                'buttons': self.buttons,
                'local_path': self.local_path[0],
                'self_path': self.local_path[1],
                'command': ''
            }

    def re_messages(self):
        with open('..\\Messages\\0_messages.txt', 'w', encoding='utf-8') as f:
            f.write("robot_name:%s\n" % self.robot_name)
            f.write("user_name:%s\n" % self.user_name)
            f.write("tuling_URL*%s\n" % self.tuling_URL)
            f.write("tuling_KEY:%s\n" % self.tuling_KEY)
            f.write("tuling_ID:%s\n" % self.tuling_ID)
            f.write('buttons:'
                    + self.buttons[0] + '.'
                    + self.buttons[1] + '.'
                    + self.buttons[2] + '.'
                    + self.buttons[3] + '.'
                    + self.buttons[4] + '.'
                    + self.buttons[5] + '\n'
                    )
            f.write("local_path:%s*%s\n" % (self.local_path[0], self.local_path[1]))

    def fresh_button(self):
        if self.buttons[0] == '0' and self.pushButton_voice.styleSheet() == "background-color: rgb(85, 255, 127);":
            self.pushButton_voice.setStyleSheet("background-color: rgb(255, 85, 0);")
        elif self.buttons[0] == '1' and self.pushButton_voice.styleSheet() == "background-color: rgb(255, 85, 0);":
            self.pushButton_voice.setStyleSheet("background-color: rgb(85, 255, 127);")
        elif self.buttons[0] == '0' and self.pushButton_voice.styleSheet() == '""':
            self.pushButton_voice.setStyleSheet("background-color: rgb(255, 85, 0);")
        elif self.buttons[0] == '1' and self.pushButton_voice.styleSheet() == '""':
            self.pushButton_voice.setStyleSheet("background-color: rgb(85, 255, 127);")
        else:
            pass

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

        if self.buttons[5] == '0' and self.pushButton_send.styleSheet() == "background-color: rgb(85, 255, 127);":
            self.pushButton_send.setStyleSheet("background-color: rgb(255, 85, 0);")
        elif self.buttons[5] == '1' and self.pushButton_send.styleSheet() == "background-color: rgb(255, 85, 0);":
            self.pushButton_send.setStyleSheet("background-color: rgb(85, 255, 127);")
        elif self.buttons[5] == '0' and self.pushButton_send.styleSheet() == '""':
            self.pushButton_send.setStyleSheet("background-color: rgb(255, 85, 0);")
        elif self.buttons[5] == '0' and self.pushButton_send.styleSheet() == '""':
            self.pushButton_send.setStyleSheet("background-color: rgb(85, 255, 127);")
        else:
            pass

    def Fresh(self):
        self.get_messages()
        self.fresh_button()

    def first_open(self):
        if self.buttons[5] == '0':
            self.buttons[5] = '1'

    def Server(self):
        try:
            Server = socket(AF_INET, SOCK_DGRAM)
            Server.bind(('127.0.0.1', 9000))
            while True:
                get, addr = Server.recvfrom(1024)
                get_lt = eval(get.decode('utf_8'))
                if get_lt['command'] == 'get_messages':
                    msg = str(self.Messages).strip().encode('utf-8')
                    Server.sendto(msg, addr)

                elif get_lt['command'] == 're_messages':
                    msg = str(self.Messages).strip().encode('utf-8')
                    Server.sendto(msg, addr)
                    self.Messages = get_lt
                    self.robot_name = self.Messages['robot_name']
                    self.user_name = self.Messages['user_name']
                    self.tuling_URL = self.Messages['tuling_URL']
                    self.tuling_KEY = self.Messages['tuling_KEY']
                    self.tuling_ID = self.Messages['tuling_ID']
                    self.buttons = self.Messages['buttons']
                    self.local_path = [self.Messages['local_path'], self.Messages['self_path']]
                    self.re_messages()
                    self.Fresh()
                elif get_lt['command'] == 'exit':
                    break

            history_write('off:' + '设置')
            self.displayTable('', '设置已关闭', 1)

        except:
            pass

    def displayTable(self, name, String, voice=0):
        if name == '':
            name = self.robot_name

        if String == '':
            String = '未加载该关键词，可以尝试打开云机器人'

        String = String.replace('[robot_name]', name).replace('[user_name]', self.user_name)

        item = QtGui.QStandardItem(name + ' : ' + String)
        self.model.setItem(self.y, 0, item)
        self.tableView.setModel(self.model)
        sleep(0.1)
        self.tableView.scrollToBottom()
        self.y += 1

        if voice == 0:
            if self.buttons[0] == '1' and name != self.user_name:
                my_Speak(String)
        else:
            pass


def show_MainWindow():
    AppSoft = QtWidgets.QApplication(argv)
    AppSoft.setWindowIcon(QtGui.QIcon('Ai.ico'))
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    exit(AppSoft.exec_())


def show_SetWindow():
    global lock_set
    if lock_set == 0:
        lock_set = 1
        thread = Thread(
            target=system,
            args=(
                '..\\venv\\Scripts\\python.exe '
                'Clever_Ai_Set.py',)
        )

        thread.start()

        threads = [thread]
        while threads:
            threads.pop().join()

        cli = socket(AF_INET, SOCK_DGRAM)
        Messages = {'command': 'exit'}
        msg = str(Messages).strip().encode('utf-8')
        cli.sendto(msg, ('127.0.0.1', 9000))
        lock_set = 0


if __name__ == '__main__':
    show_MainWindow()
