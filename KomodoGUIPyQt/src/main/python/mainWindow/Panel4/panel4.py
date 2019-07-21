from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys
import MySQLdb
import os
from src.main.python import common, login, register
from src.main.python.mainWindow import mainWindow


def miniGame(self, stack4):
    layout_4 = QFormLayout()
    ttt_game_frame = QFrame()
    ttt_game_frame.setFixedSize(350, 380)
    ttt_game_form = QGridLayout()
    ttt_game_frame.setLayout(ttt_game_form)

    ttt_gamebtn_1 = QPushButton()
    ttt_gamebtn_1.setFixedSize(100, 100)
    ttt_game_form.addWidget(ttt_gamebtn_1, 0, 0)
    ttt_gamebtn_2 = QPushButton()
    ttt_gamebtn_2.setFixedSize(100, 100)
    ttt_game_form.addWidget(ttt_gamebtn_2, 0, 1)
    ttt_gamebtn_3 = QPushButton()
    ttt_gamebtn_3.setFixedSize(100, 100)
    ttt_game_form.addWidget(ttt_gamebtn_3, 0, 2)

    ttt_gamebtn_4 = QPushButton()
    ttt_gamebtn_4.setFixedSize(100, 100)
    ttt_game_form.addWidget(ttt_gamebtn_4, 1, 0)
    ttt_gamebtn_5 = QPushButton()
    ttt_gamebtn_5.setFixedSize(100, 100)
    ttt_game_form.addWidget(ttt_gamebtn_5, 1, 1)
    ttt_gamebtn_6 = QPushButton()
    ttt_gamebtn_6.setFixedSize(100, 100)
    ttt_game_form.addWidget(ttt_gamebtn_6, 1, 2)

    ttt_gamebtn_7 = QPushButton()
    ttt_gamebtn_7.setFixedSize(100, 100)
    ttt_game_form.addWidget(ttt_gamebtn_7, 2, 0)
    ttt_gamebtn_8 = QPushButton()
    ttt_gamebtn_8.setFixedSize(100, 100)
    ttt_game_form.addWidget(ttt_gamebtn_8, 2, 1)
    ttt_gamebtn_9 = QPushButton()
    ttt_gamebtn_9.setFixedSize(100, 100)
    ttt_game_form.addWidget(ttt_gamebtn_9, 2, 2)

    # self.setTabText(0,"Contact Details")
    layout_4.addRow(ttt_game_frame)
    stack4.setLayout(layout_4)