#!/usr/bin/env python2
# encoding: utf-8
# @Auther     :   yjz
# @File       :   main.py
# @Time       :   2020/2/3 14:23
# @Version    :   0.1
# @Function  :   主要界面显示


from login.main_window import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from Parser.parser import getProblemset, getProblem, getStatus
from view.pro_window import Pro_Window
from view.submit_window import Sub_Window, headers
from view.status_window import statusDialog

status_url = 'http://acm.hdu.edu.cn/status.php?user='
submit_url = 'http://acm.hdu.edu.cn/submit.php?action=submit'


# 主窗口类
class Main_Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        # 信号槽事件相连
        self.pid = None
        self.session = None
        self.sub = None
        self.user = None
        self.sta=None
        self.Num1.clicked.connect(lambda: self.Jump_func_thread(self.Num1.text()))
        self.Num2.clicked.connect(lambda: self.Jump_func_thread(self.Num2.text()))
        self.Num3.clicked.connect(lambda: self.Jump_func_thread(self.Num3.text()))
        self.Num4.clicked.connect(lambda: self.Jump_func_thread(self.Num4.text()))
        self.Num5.clicked.connect(lambda: self.Jump_func_thread(self.Num5.text()))

    # 翻页功能
    def Jump_func(self, session, url):
        '''
        :param session: 带有登录信息session
        :param url: 需要获取问题的网址
        :return:返回解析后的问题集合
        '''
        contents = session.get(url).content
        problem_set = getProblemset(contents)
        return problem_set

    # 原有的weight创建数据
    def set_data(self, problem_set):
        '''
        :param problem_set: 问题集合，为list，第一项为问题名字，第二项为对应的相关信息：'问题ID','提交次数','总通过次数','总提交次数'
        :return:None
        '''
        self.tableWidget.setRowCount(len(problem_set))
        self.tableWidget.setColumnCount(len(problem_set[1]))
        self.tableWidget.setHorizontalHeaderLabels(['问题ID', '提交次数', '问题名称', '总通过次数', '总提交次数'])
        self.tableWidget.verticalHeader().setVisible(False)
        # 列宽自适用大小
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        # 遍历问题集合，将button加入其中
        for i in range(len(problem_set)):
            button = self.createButton(problem_set[i][0])

            self.tableWidget.setCellWidget(i, 0, button)
            for j in range(1, len(problem_set[i])):
                item = QTableWidgetItem(problem_set[i][j])
                # 设置文字居中
                item.setTextAlignment(4)
                item.setFlags(Qt.ItemIsEditable)
                self.tableWidget.setItem(i, j, item)

        # self.tableWidget.add

    def createButton(self, pid):
        # 添加按钮，使之能跳转
        button = QPushButton()
        button.setStyleSheet('''
                               text-align:center;
                               background-color:LightCoral;
                               height:30px;
                               border-style:outset;
                               font:13px;
                           ''')
        button.setText(pid)
        button.clicked.connect(lambda: self.lookProblem_func_thread(button.text()))
        return button

    # 翻页功能
    def Jump_func_thread(self, num):
        '''
        :param num: 需要翻到的页数
        :return:None
        '''
        url = 'http://acm.hdu.edu.cn/listproblem.php?vol=' + num
        if int(num) > 2:
            self.Num1.setText(str(int(num) - 2))
            self.Num2.setText(str(int(num) - 1))
            self.Num3.setText(str(num))
            self.Num4.setText(str(int(num) + 1))
            self.Num5.setText(str(int(num) + 2))
        thread = RunThread(func=self.Jump_func, session=self.session, url=url)
        thread.trigger.connect(self.set_data)
        thread.start()
        while True:
            QApplication.processEvents()
            if thread.flag == 1:
                break

    # c查看问题线程模块
    def lookProblem_func_thread(self, pid):
        '''

        :param pid: 需要传递问题id，方便组合网页地址
        :return:None
        '''
        self.pid = pid
        print(pid)
        url = 'http://acm.hdu.edu.cn/showproblem.php?pid=' + pid
        thread = RunThread(func=self.look_func, session=self.session, url=url)
        thread.trigger.connect(self.pro_window)
        thread.trigger.connect(self.sub_window)
        thread.start()
        while True:
            QApplication.processEvents()
            if thread.flag == 1:
                break

    # 查看问题
    def look_func(self, session, url):
        contents = session.get(url).content.decode('gb2312')
        content = getProblem(contents)
        return content

    # 问题窗口
    def pro_window(self, data):
        '''

        :param data:问题信息,type为list,[问题描述，问题输入，问题输出，样例输入，样例输出]
        :return:None
        '''
        pro = Pro_Window()
        pro.descripBrowser.setText(data[0])
        pro.inputBrowser.setText(data[1])
        pro.outputBrowser.setText(data[2])
        pro.sampleInputBrowser.setText(data[3])
        pro.sampleOutputBrowser.setText(data[4])
        pro.setWindowModality(1)
        pro.exec_()

    # 提交问题窗口
    def sub_window(self):
        '''

        :return:None
        '''
        sub = Sub_Window()
        self.sub = sub
        sub.pid = self.pid
        sub.session = self.session
        sub.setWindowFlag(Qt.WindowMaximizeButtonHint)
        sub.setWindowFlag(Qt.WindowMinimizeButtonHint)
        sub.setWindowFlag(Qt.WindowCloseButtonHint)
        sub.pushButton.clicked.connect(self.submit_func_thread)
        sub.pushButton.clicked.connect(self.view_dialog_thread)
        sub.setWindowModality(1)
        sub.exec_()

    def submit_func_thread(self):
        '''

        :return:None
        '''
        thread = RunThread(func=self.submit_func, session=self.session, url=submit_url)
        thread.trigger.connect(self.submit_status)
        thread.start()
        while True:
            QApplication.processEvents()
            if thread.flag == 1:
                break

    def submit_status(self, status_code):
        '''

        :param status_code状态码
        :return:
        '''
        print(status_code)

    def submit_func(self, session, url):
        usercode = self.sub.codeEdit.toPlainText()
        data = {
            'check': 0,
            'problemid': int(self.pid),
            'language': 2,
            'usercode': usercode
        }
        con = session.post(url, headers=headers, data=data)
        self.sta=None
        return con.status_code

    def view_dialog_thread(self):
        '''

        :return: None
        '''
        thread = RunThread(func=self.view_status, session=self.session, url=status_url + self.user)
        thread.trigger.connect(self.status_display)
        thread.start()
        while True:
            QApplication.processEvents()
            if thread.flag == 1:
                break

    def view_status(self, session, status_url):
        '''

        :param session: 含有cookie得到会话
        :param status_url: 查询状态的网址
        :return:
        '''
        content = session.get(status_url, headers=headers).content.decode('gb2312')
        data = getStatus(content)
        return data

    # 展示状态
    def status_display(self, data):
        '''

        :param data: 返回数据，list，每一个元素包含一个list[’运行id','提交时间','提交状态'.....]
        :return:
        '''
        if self.sta:
            status_w=self.sta
        else:
            status_w = statusDialog()
            self.sta=status_w

        status_w.setWindowFlag(Qt.WindowMaximizeButtonHint)
        status_w.setWindowFlag(Qt.WindowMinimizeButtonHint)
        status_w.setWindowFlag(Qt.WindowCloseButtonHint)
        status_w.tableWidget.setRowCount(len(data))
        status_w.tableWidget.setColumnCount(len(data[0]))
        status_w.tableWidget.verticalHeader().setVisible(False)
        status_w.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        status_w.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        for i in range(len(data)):
            for j in range(len(data[i])):
                item = QTableWidgetItem(data[i][j])
                item.setTextAlignment(4)
                item.setFlags(Qt.ItemIsEditable)
                status_w.tableWidget.setItem(i, j, item)

        status_w.pushButton.clicked.connect(self.view_dialog_thread)
        status_w.setWindowModality(1)
        status_w.exec_()


# 线程运行,专门供给目前项目
class RunThread(QThread):
    trigger = pyqtSignal(list)

    def __init__(self, func, session, parent=None, url=None, data=None):
        self.func = func
        self.session = session
        self.url = url
        self.data = data
        self.flag = 0
        super(RunThread, self).__init__(parent)

    def __del__(self):
        self.wait()

    def run(self):
        if self.func != None:
            try:
                if self.data == None:
                    d = self.func(self.session, self.url)
                else:
                    d = self.func(self.session, self.data, self.url)
                self.flag = 1
                self.trigger.emit(d)
                self.quit()
            except:
                self.flag = 1
                pass

    # def callback(self, msg):
    #     # 信号焕发，我是通过我封装类的回调来发起的
    #     # self._signal.emit(msg)
    #     print(msg)
