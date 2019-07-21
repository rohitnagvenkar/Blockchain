from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from src.main.python import common


class Register(QWidget):
    switch_window = QtCore.pyqtSignal(str, str)

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Register')
        self.resize(580, 800)
        self.setFixedSize(580, 800)

        registerFrame = QFrame(self)
        registerFrame.setStyleSheet("background-color: rgb(255,255,255); margin:5px; border:1px solid rgb(0, 255, 0); ")
        registerFrame.setGeometry(10, 10, 560, 780)

        formRegister = QFormLayout()

        lbl_registerFrame = QFrame()
        lbl_formRegister = QFormLayout()
        lbl_register = QLabel("Create an account")
        lbl_register.setStyleSheet("font-size: 20px")
        lbl_register.setAlignment(QtCore.Qt.AlignCenter)
        lbl_formRegister.addRow(lbl_register)
        lbl_registerFrame.setLayout(lbl_formRegister)
        formRegister.addRow(lbl_registerFrame)

        gf_btn_Frame = QFrame()
        gf_btn_FrameForm = QFormLayout()
        google_btn_login = QPushButton(gf_btn_Frame)
        google_btn_login.setText("Google")
        google_btn_login.setMinimumHeight(40)
        google_btn_login.setMinimumWidth(250)
        facebook_btn_login = QPushButton(gf_btn_Frame)
        facebook_btn_login.setText("Facebook")
        facebook_btn_login.setMinimumHeight(40)
        facebook_btn_login.setMinimumWidth(250)
        gf_btn_FrameForm.addRow(google_btn_login, facebook_btn_login)
        gf_btn_Frame.setLayout(gf_btn_FrameForm)

        filler_lbl_register = QLabel()
        filler_lbl_register.setText("-------------------------------------------------     OR     --------------------------------------------------")
        gf_btn_FrameForm.addRow(filler_lbl_register)

        filler_lbl2_register = QLabel()
        filler_lbl2_register.setText("Start your bitcoin transactions with a Komodo Account")
        gf_btn_FrameForm.addRow(filler_lbl2_register)

        self.country_cb_register = QComboBox()
        self.country_cb_register.addItem("United States")
        self.country_cb_register.addItem("B")
        self.country_cb_register.addItem("C")
        self.country_cb_register.addItem("D")
        self.country_cb_register.addItem("E")
        self.country_cb_register.currentIndexChanged.connect(self.selectionchange)
        self.country_cb_register.setMinimumHeight(40)
        gf_btn_FrameForm.addRow(self.country_cb_register)

        self.firstname_txt_register = QLineEdit(gf_btn_Frame)
        self.firstname_txt_register.setMinimumWidth(250)
        self.firstname_txt_register.setMinimumHeight(40)
        self.firstname_txt_register.setPlaceholderText("First Name")

        self.lastname_txt_register = QLineEdit(gf_btn_Frame)
        self.lastname_txt_register.setMinimumWidth(250)
        self.lastname_txt_register.setMinimumHeight(40)
        self.lastname_txt_register.setPlaceholderText("Last Name")
        gf_btn_FrameForm.addRow(self.firstname_txt_register, self.lastname_txt_register)

        self.email_txt_register = QLineEdit(gf_btn_Frame)
        self.email_txt_register.setMinimumHeight(40)
        self.email_txt_register.setPlaceholderText("Email")
        gf_btn_FrameForm.addRow(self.email_txt_register)

        self.password_txt_register = QLineEdit(gf_btn_Frame)
        self.password_txt_register.setMinimumHeight(40)
        self.password_txt_register.setPlaceholderText("Password")
        self.password_txt_register.setEchoMode(QLineEdit.Password)
        gf_btn_FrameForm.addRow(self.password_txt_register)

        self.questions_cb_register = QComboBox()
        self.questions_cb_register.addItem("Select a Question")
        self.questions_cb_register.addItem("B")
        self.questions_cb_register.addItem("C")
        self.questions_cb_register.addItem("D")
        self.questions_cb_register.addItem("E")
        self.questions_cb_register.currentIndexChanged.connect(self.selectionchange)
        self.questions_cb_register.setMinimumHeight(40)
        gf_btn_FrameForm.addRow(self.questions_cb_register)

        self.answer_txt_register = QLineEdit(gf_btn_Frame)
        self.answer_txt_register.setMinimumHeight(40)
        self.answer_txt_register.setPlaceholderText("Secret Answer")
        gf_btn_FrameForm.addRow(self.answer_txt_register)

        formRegister.addRow(gf_btn_Frame)

        check_email_Frame = QFrame()
        emailformCheck = QFormLayout()
        self.checkEmail = QCheckBox("Receive news and special offers from Komodo by email.")
        self.checkEmail.setChecked(False)
        self.checkEmail.toggled.connect(lambda: self.btnstate(self.checkEmail))
        emailformCheck.addRow(self.checkEmail)
        check_email_Frame.setLayout(emailformCheck)
        formRegister.addRow(check_email_Frame)

        submit_btn_register = QPushButton(registerFrame)
        submit_btn_register.setText("Create a free account")
        submit_btn_register.setMinimumHeight(40)
        formRegister.addRow(submit_btn_register)

        clear_btn_register = QPushButton(registerFrame)
        clear_btn_register.setText("Already have an account?")
        clear_btn_register.setMinimumHeight(40)
        formRegister.addRow(clear_btn_register)

        submit_btn_register.clicked.connect(self.mainWindow)
        clear_btn_register.clicked.connect(self.login)

        lbl_register_terms = QLabel()
        lbl_register_terms.setText("By clicking on \"Create a free account\", I agree to the Komodo End User Licence Agreement and Privacy Policy")
        lbl_register_terms.setWordWrap(True)
        formRegister.addRow(lbl_register_terms)

        registerFrame.setLayout(formRegister)

    def login(self):
        self.switch_window.emit("login")

    def mainWindow(self):
        ucheck = False
        pcheck = False
        if self.email_txt_register.text() == "":
            self.email_txt_register.setPlaceholderText("email is empty")
            self.email_txt_register.setStyleSheet("border: 2px solid orange;")
        else:
            ucheck = True

        if self.password_txt_register.text() == "":
            self.password_txt_register.setPlaceholderText("password is empty")
            self.password_txt_register.setStyleSheet("border: 2px solid orange;")
        else:
            pcheck = True

        if ucheck and pcheck:
            if common.submit_Function_Login(self, self.email_txt_register.text(), self.password_txt_register.text(), "existsR"):
                error = common.submit_Function_Register(self, self.email_txt_register.text(), self.password_txt_register.text(), self.country_cb_register.currentText(), self.firstname_txt_register.text(), self.lastname_txt_register.text(), self.questions_cb_register.currentIndex(), self.answer_txt_register.text(), self.checkEmail.checkState())
                if error:
                    print("Unable to connect to the database at the moment")
                else:
                    self.switch_window.emit("mainWindow", self.email_txt_register.text())
            else:
                self.email_txt_register.clear()
                self.email_txt_register.setPlaceholderText("username is already present")
                self.email_txt_register.setStyleSheet("border: 2px solid red;")

    def btnstate(self, b):
        if b.isChecked():
            print(b.text() + " is selected")
        else:
            print(b.text() + " is deselected")

    def selectionchange(self, i):
        print("Items in the list are :")
