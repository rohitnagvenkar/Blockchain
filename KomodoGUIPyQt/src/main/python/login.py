from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import os
from src.main.python import common


class Login(QWidget):
    switch_window = QtCore.pyqtSignal(str, str)

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Login')
        self.resize(400, 500)
        self.setFixedSize(400, 500)

        loginFrame = QFrame(self)
        loginFrame.setStyleSheet("background-color: rgb(255,255,255); margin:5px; border:1px solid rgb(0, 255, 0); ")
        loginFrame.setGeometry(10, 10, 380, 480)

        formLogin = QFormLayout()

        self.username_txt_login = QLineEdit()
        self.username_txt_login.setMinimumHeight(40)
        self.username_txt_login.setPlaceholderText("username")
        formLogin.addRow(self.username_txt_login)

        self.password_txt_login = QLineEdit()
        self.password_txt_login.setEchoMode(QLineEdit.Password)
        self.password_txt_login.setPlaceholderText("password")
        self.password_txt_login.setMinimumHeight(40)
        formLogin.addRow(self.password_txt_login)

        checkFrame = QFrame()
        formCheck = QFormLayout()
        self.check = QCheckBox("Keep me logged in")
        self.check.setChecked(False)
        self.check.toggled.connect(lambda: self.btnstate(self.check))
        formCheck.addRow(self.check)
        checkFrame.setLayout(formCheck)
        formLogin.addRow(checkFrame)

        submit_btn_login = QPushButton(loginFrame)
        submit_btn_login.setText("Login to Komodo App")
        submit_btn_login.setMinimumHeight(40)
        formLogin.addRow(submit_btn_login)

        labelFrame = QFrame()
        labelFrameForm = QFormLayout()
        lbl_filler = QLabel("------------------   OR LOGIN WITH   --------------------------------")
        labelFrameForm.addRow(lbl_filler)
        labelFrame.setLayout(labelFrameForm)
        formLogin.addRow(labelFrame)

        gf_btn_Frame = QFrame()
        gf_btn_FrameForm = QFormLayout()
        google_btn_login = QPushButton(gf_btn_Frame)
        google_btn_login.setText("Google")
        google_btn_login.setMinimumHeight(40)
        google_btn_login.setMinimumWidth(150)
        facebook_btn_login = QPushButton(gf_btn_Frame)
        facebook_btn_login.setText("Facebook")
        facebook_btn_login.setMinimumHeight(40)
        facebook_btn_login.setMinimumWidth(150)
        gf_btn_FrameForm.addRow(google_btn_login, facebook_btn_login)
        gf_btn_Frame.setLayout(gf_btn_FrameForm)
        formLogin.addRow(gf_btn_Frame)

        clear_btn_login = QPushButton(loginFrame)
        clear_btn_login.setText("Create a free Blizzard Account")
        clear_btn_login.setMinimumHeight(40)
        formLogin.addRow(clear_btn_login)

        self.m_label_gif = QLabel()
        self.m_loading_gif = QtGui.QMovie("./images/loading.gif")
        self.m_label_gif.setMovie(self.m_loading_gif)
        self.m_label_gif.setScaledContents(False)
        self.m_loading_gif.start()
        self.m_label_gif.show()
        formLogin.addRow(self.m_label_gif)

        submit_btn_login.clicked.connect(self.mainWindow)
        clear_btn_login.clicked.connect(self.register)

        loginFrame.setLayout(formLogin)

    def btnstate(self, b):
        if b.isChecked():
            print(b.text() + " is selected")
        else:
            print(b.text() + " is deselected")

    def register(self):
        self.switch_window.emit("register", "")

    def mainWindow(self):
        ucheck = False
        pcheck = False
        if self.username_txt_login.text() == "":
            self.username_txt_login.setPlaceholderText("username is empty")
            self.username_txt_login.setStyleSheet("border: 2px solid orange;")
        else:
            ucheck = True

        if self.password_txt_login.text() == "":
            self.password_txt_login.setPlaceholderText("password is empty")
            self.password_txt_login.setStyleSheet("border: 2px solid orange;")
        else:
            pcheck = True

        if ucheck and pcheck:
            if common.submit_Function_Login(self, self.username_txt_login.text(), self.password_txt_login.text(), "existsL"):
                self.username_txt_login.setPlaceholderText("username incorrect")
                self.username_txt_login.setStyleSheet("border: 2px solid red;")
                self.password_txt_login.setPlaceholderText("password incorrect")
                self.password_txt_login.setStyleSheet("border: 2px solid red;")
            else:
                if self.check.checkState() == 2:
                    path = './home/.komodoGUI/'
                    writepath = './home/.komodoGUI/settings.dat'
                    if os.path.exists(writepath):
                        mode = 'w'
                        with open(writepath, mode) as f:
                            f.write('{\n' +
                                    '"username": "' + self.username_txt_login.text() +
                                    '",\n' +
                                    '"password": "' + self.password_txt_login.text() +
                                    '"\n' +
                                    '}')
                    else:
                        try:
                            original_umask = os.umask(0)
                            os.makedirs(path, 0o777)
                            mode = 'w'
                            with open(writepath, mode) as f:
                                f.write('Hello, world!\n')
                        except OSError:
                            print("Creation of the directory %s failed" % path)
                        finally:
                            os.umask(original_umask)
                    self.switch_window.emit("mainWindow_fromLogin", self.username_txt_login.text())
                else:
                    self.switch_window.emit("mainWindow_fromLogin", self.username_txt_login.text())