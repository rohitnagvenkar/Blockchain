from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys
import MySQLdb
import os
from src.main.python import common, login, register
from src.main.python.mainWindow import mainWindow


def tutorial(self, stack2):
    layout_2 = QFormLayout()
    layout_2.addRow("Male", QLineEdit())
    layout_2.addRow("Female", QLineEdit())
    # self.setTabText(0,"Contact Details")
    stack2.setLayout(layout_2)