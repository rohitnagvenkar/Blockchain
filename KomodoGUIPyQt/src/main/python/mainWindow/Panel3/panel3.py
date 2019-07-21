from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys
import MySQLdb
import os
from src.main.python import common, login, register
from src.main.python.mainWindow import mainWindow


def chatApp(self, stack3):
    # HOST = "127.0.0.1"
    # PORT = 33000
    # self.BUFSIZ = 1024
    # ADDR = (HOST, PORT)
    # self.client_socket = socket(AF_INET, SOCK_STREAM)
    # self.client_socket.connect(ADDR)

    # receive_thread = Thread(target=self.receive)
    # receive_thread.start()

    layout_3 = QFormLayout()
    self.viewbox_chat_txt = QPlainTextEdit()
    self.viewbox_chat_txt.setFixedSize(900, 380)
    self.viewbox_chat_txt.setEnabled(False)
    layout_3.addRow(self.viewbox_chat_txt)
    sendmsg_chat_txt = QLineEdit()
    sendmsg_chat_txt.setPlaceholderText("Type your message...")
    sendmsg_chat_txt.setMinimumHeight(40)
    sendmsg_chat_txt.setMinimumWidth(700)
    sendmsg_chat_btn = QPushButton()
    sendmsg_chat_btn.setText("Send")
    sendmsg_chat_btn.setMinimumHeight(40)
    sendmsg_chat_btn.clicked.connect(lambda: self.send(sendmsg_chat_txt.text()))
    layout_3.addRow(sendmsg_chat_txt, sendmsg_chat_btn)
    stack3.setLayout(layout_3)


