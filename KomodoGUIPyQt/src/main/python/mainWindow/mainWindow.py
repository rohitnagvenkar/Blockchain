from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys
import MySQLdb
import os
from src.main.python import common, login, register
from src.main.python.mainWindow.Panel1 import panel1
from src.main.python.mainWindow.Panel2 import panel2
from src.main.python.mainWindow.Panel3 import panel3
from src.main.python.mainWindow.Panel4 import panel4


class MainWindow(QWidget):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, user):
        QWidget.__init__(self)
        self.setWindowTitle('Komodo Control Panel')
        self.resize(1200, 750)
        self.setFixedSize(1200, 750)

        mainFrame = QFrame(self)
        mainFrame_Form = QGridLayout()
        mainFrame.setGeometry(0, 0, 1200, 750)
        mainFrame.setStyleSheet("background-color: rgb(255,255,255); margin:5px; border:1px solid rgb(0, 255, 0); ")

        acc_mainFrame = QFrame()
        acc_mainFrame.setGeometry(0, 0, 200, 750)
        accFrame_Form = QFormLayout()
        lbl0 = QLabel()
        lbl0.setText("Komodo")
        acc_mainFrame.setLayout(accFrame_Form)
        lbl_accFrame_Form = QLabel()
        lbl_accFrame_Form.setText("Welcome " + user)
        accFrame_Form.addWidget(lbl_accFrame_Form)

        mainFrame_Form.addWidget(acc_mainFrame, 0, 0, 1, 2)

        self.console_mainFrame = QFrame()
        self.console_mainFrame_txtarea = QTextEdit(self.console_mainFrame)
        self.console_mainFrame_txtarea.setFixedSize(940, 200)
        self.console_mainFrame_txtarea.append("Hello")
        self.console_mainFrame_txtarea.setStyleSheet("background: #333333; color: white")
        self.console_mainFrame.setFixedSize(940, 200)

        content_mainFrame = QFrame()
        content_mainFrame.setFixedSize(940, 450)
        stack = QStackedWidget(content_mainFrame)
        stack1 = QWidget()
        stack2 = QWidget()
        stack3 = QWidget()
        stack4 = QWidget()

        panel1.komodo(self, stack1, self.console_mainFrame_txtarea)
        panel2.tutorial(self, stack2)
        panel3.chatApp(self, stack3)
        panel4.miniGame(self, stack4)

        stack.addWidget(stack1)
        stack.addWidget(stack2)
        stack.addWidget(stack3)
        stack.addWidget(stack4)

        menu_mainFrame = QFrame()
        menu_mainFrame.setFixedSize(220, 650)
        menuFrame_Form = QFormLayout()
        lbl1 = QPushButton()
        lbl1.setText("Komodo")
        lbl1.clicked.connect(lambda: self.display(stack, 0))
        lbl2 = QPushButton()
        lbl2.setText("Tutorial")
        lbl2.clicked.connect(lambda: self.display(stack, 1))
        lbl3 = QPushButton()
        lbl3.setText("Chat")
        lbl3.clicked.connect(lambda: self.display(stack, 2))
        lbl4 = QPushButton()
        lbl4.setText("Game")
        lbl4.clicked.connect(lambda: self.display(stack, 3))
        lbl5 = QPushButton()
        lbl5.setText("watch Videos")
        lbl6 = QPushButton()
        lbl6.setText("Comming soon...")
        menuFrame_Form.addRow(lbl1)
        menuFrame_Form.addRow(lbl2)
        menuFrame_Form.addRow(lbl3)
        menuFrame_Form.addRow(lbl4)
        menuFrame_Form.addRow(lbl5)
        menuFrame_Form.addRow(lbl6)
        menu_mainFrame.setLayout(menuFrame_Form)
        #mainFrame_Form.addRow(menu_mainFrame, content_mainFrame)
        mainFrame_Form.addWidget(menu_mainFrame, 1, 0, 2, 1)
        mainFrame_Form.addWidget(content_mainFrame, 1, 1, 1, 1)
        mainFrame_Form.addWidget(self.console_mainFrame, 2, 1, 1, 1)
        mainFrame.setLayout(mainFrame_Form)

    def display(self, stack, i):
        stack.setCurrentIndex(i)
