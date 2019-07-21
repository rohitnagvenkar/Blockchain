from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys
import MySQLdb
import os


def submit_Function_Login(self, uname, pwd, condition):
    if condition == "existsL":
        sql = """SELECT * FROM komodoGUI.accounts WHERE username = '%s' AND password = '%s'""" % (uname, pwd)
    else:
        sql = """SELECT * FROM komodoGUI.accounts WHERE username = '%s'""" % uname

    dbconnect = MySQLdb.connect("3.16.180.203", "myname", "mypassword", "komodoGUI")
    cursor = dbconnect.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    if data:
        print(data)
        echeck = False
    else:
        print(data)
        echeck = True
    cursor.close()
    dbconnect.close()
    return echeck



def submit_Function_Register(self, uname, pwd, country, firstname, lastname, sec_q, sec_ans, extra):
    try:
        print(uname, pwd, country, firstname, lastname, sec_q, sec_ans, extra)
        sql = """INSERT INTO komodoGUI.accounts (username, password, country, firstname, lastname, sec_q, sec_ans, extra) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')""" % (uname, pwd, country, firstname, lastname, sec_q, sec_ans, extra)
        print(sql)
        dbconnect = MySQLdb.connect("3.16.180.203", "myname", "mypassword", "komodoGUI")
        cursor = dbconnect.cursor()
        cursor.execute(sql)
        dbconnect.commit()
        print("Record inserted successfully into python_users table")

    except dbconnect.Error:
        dbconnect.rollback()  # rollback if any exception occured
        echeck = True
        return echeck

    finally:
        if dbconnect.open:
            echeck = False
            cursor.close()
            dbconnect.close()
            print("MySQL connection is closed")
            return echeck

def receive(self):
    while True:
        try:
            msg = self.client_socket.recv(self.BUFSIZ).decode("utf8")
            self.viewbox_chat_txt.appendPlainText(msg)
            # add received msg in your text area
        except OSError:
            break

def send(self, text):
    if text is None:
        msg = ""
    else:
        msg = text
    self.client_socket.send(bytes(text, "utf8"))
    if text == "{quit}":
        self.client_socket.close()
