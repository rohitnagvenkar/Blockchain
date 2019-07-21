from PyQt5.QtWidgets import *
from src.main.python.mainWindow.Panel1 import panel1_functions
from PyQt5 import QtCore


def komodo(self, stack1, console_txt):
    layout_komodo = QFormLayout()



    layout_connect_frame = QFrame()
    layout_connect_frame.setFixedSize(340, 420)
    layout_connect = QFormLayout()
    layout_connect_frame.setLayout(layout_connect)

    layout_utilities_frame = QFrame()
    layout_utilities = QGridLayout()
    layout_utilities_frame.setFixedSize(560, 420)
    layout_utilities_frame.setLayout(layout_utilities)

    hostname_txt = QLineEdit()
    hostname_txt.setPlaceholderText("Enter the host name")
    hostname_txt.setMinimumHeight(40)
    hostname_txt.setMaximumWidth(330)
    layout_connect.addRow(hostname_txt)

    hostport_txt = QLineEdit()
    hostport_txt.setPlaceholderText("Enter the host port number")
    hostport_txt.setMinimumHeight(40)
    hostport_txt.setMaximumWidth(330)
    layout_connect.addRow(hostport_txt)

    hostusername_txt = QLineEdit()
    hostusername_txt.setPlaceholderText("Enter the host username")
    hostusername_txt.setMinimumHeight(40)
    hostusername_txt.setMaximumWidth(330)
    layout_connect.addRow(hostusername_txt)

    hostpassword_txt = QLineEdit()
    hostpassword_txt.setPlaceholderText("Enter the host password")
    hostpassword_txt.setMinimumHeight(40)
    hostpassword_txt.setMaximumWidth(330)
    hostpassword_txt.setEchoMode(QLineEdit.Password)
    layout_connect.addRow(hostpassword_txt)

    komodo_submit_btn = QPushButton()
    komodo_submit_btn.setText("Connect")
    komodo_submit_btn.setMinimumWidth(150)
    komodo_submit_btn.setMinimumHeight(40)

    #console_mainFrame_txtarea
    komodo_clear_btn = QPushButton()
    komodo_clear_btn.setText("Clear")
    komodo_clear_btn.setMinimumWidth(150)
    komodo_clear_btn.setMinimumHeight(40)

    layout_connect.addRow(komodo_submit_btn, komodo_clear_btn)

    info_lbl = QLabel()
    info_lbl.setText("--------------------------------------------------------------------")
    layout_connect.addRow(info_lbl)

    senderaddr_txt = QLineEdit()
    senderaddr_txt.setPlaceholderText("Enter senders address")
    senderaddr_txt.setMinimumHeight(40)
    senderaddr_txt.setMaximumWidth(330)
    layout_connect.addRow(senderaddr_txt)

    kmdamount_txt = QLineEdit()
    kmdamount_txt.setPlaceholderText("Enter the KMD amount")
    kmdamount_txt.setMinimumHeight(40)
    kmdamount_txt.setMaximumWidth(330)
    layout_connect.addRow(kmdamount_txt)

    extrainfo_txt = QLineEdit()
    extrainfo_txt.setPlaceholderText("Enter extra info")
    extrainfo_txt.setMinimumHeight(40)
    extrainfo_txt.setMaximumWidth(330)
    layout_connect.addRow(extrainfo_txt)

    #form 2 utilities section.................................................................

    getbalance_btn_utilities = QHoverButton()
    getbalance_btn_utilities.setText("Get Balance")
    getbalance_btn_utilities.setMinimumHeight(40)
    getbalance_btn_utilities.setMaximumWidth(250)

    layout_utilities.addWidget(getbalance_btn_utilities, 0, 0, 1, 1)

    genaddr_btn_utilities = QHoverButton()
    genaddr_btn_utilities.setText("Generate Address")
    genaddr_btn_utilities.setMinimumHeight(40)
    genaddr_btn_utilities.setMaximumWidth(250)

    layout_utilities.addWidget(genaddr_btn_utilities, 1, 0, 1, 1)

    sendtoaddr_btn_utilities = QHoverButton()
    sendtoaddr_btn_utilities.setText("Send to Address")
    sendtoaddr_btn_utilities.setMinimumHeight(40)
    sendtoaddr_btn_utilities.setMaximumWidth(250)

    layout_utilities.addWidget(sendtoaddr_btn_utilities, 2, 0, 1, 1)

    gettansinfo_btn_utilities = QHoverButton()
    gettansinfo_btn_utilities.setText("Get Transaction Info")
    gettansinfo_btn_utilities.setMinimumHeight(40)
    gettansinfo_btn_utilities.setMaximumWidth(250)

    layout_utilities.addWidget(gettansinfo_btn_utilities, 3, 0, 1, 1)

    valaddr_btn_utilities = QHoverButton()
    valaddr_btn_utilities.setText("Validate Address")
    valaddr_btn_utilities.setMinimumHeight(40)
    valaddr_btn_utilities.setMaximumWidth(250)

    layout_utilities.addWidget(valaddr_btn_utilities, 4, 0, 1, 1)

    getnetinfo_btn_utilities = QHoverButton()
    getnetinfo_btn_utilities.setText("Get Network Info")
    getnetinfo_btn_utilities.setMinimumHeight(40)
    getnetinfo_btn_utilities.setMinimumWidth(250)
    getnetinfo_btn_utilities.setMaximumWidth(250)

    layout_utilities.addWidget(getnetinfo_btn_utilities, 5, 0, 1, 1)

    addnode_btn_utilities = QHoverButton()
    addnode_btn_utilities.setText("Add a new Node")
    addnode_btn_utilities.setMinimumHeight(40)
    addnode_btn_utilities.setMaximumWidth(250)

    layout_utilities.addWidget(addnode_btn_utilities, 6, 0, 1, 1)

    getwalletinfo_btn_utilities = QHoverButton()
    getwalletinfo_btn_utilities.setText("Get Wallet Info")
    getwalletinfo_btn_utilities.setMinimumHeight(40)
    getwalletinfo_btn_utilities.setMaximumWidth(250)

    layout_utilities.addWidget(getwalletinfo_btn_utilities, 7, 0, 1, 1)

    getblockinfo_btn_utilities = QHoverButton()
    getblockinfo_btn_utilities.setText("Get Blockchain Info")
    getblockinfo_btn_utilities.setMinimumHeight(40)
    getblockinfo_btn_utilities.setMaximumWidth(250)
    #getblockinfo_btn_utilities.clicked.connect(lambda: panel1_functions.btn_9())
    #layout_utilities.addWidget(getblockinfo_btn_utilities, 7, 0, 1, 1)


    listaddrs_frame = QFrame()
    listaddrs_form = QFormLayout()
    listaddrs_form.setSpacing(0)
    listaddrs_frame.setLayout(listaddrs_form)
    addresseslbl_lbl_utilities = QLabel()
    addresseslbl_lbl_utilities.setText("List of your addresses:- ")
    listaddrs_form.addRow(addresseslbl_lbl_utilities)
    listaddr_listbox_utilities = QListWidget()
    listaddrs_form.addRow(listaddr_listbox_utilities)
    layout_utilities.addWidget(listaddrs_frame, 0, 1, 4, 1)

    getbtninfo_frame = QFrame()
    getbtninfo_form = QFormLayout()
    getbtninfo_form.setSpacing(0)
    getbtninfo_frame.setLayout(getbtninfo_form)
    btninfolbl_lbl_utilities = QLabel()
    btninfolbl_lbl_utilities.setText("Information:- ")
    getbtninfo_form.addRow(btninfolbl_lbl_utilities)
    btninfo_txt_utilities = QTextEdit()
    textstr = "Get Balance: \n\n" \
              "This method returns the server's total available balance."
    btninfo_txt_utilities.setText(textstr)
    getbtninfo_form.addRow(btninfo_txt_utilities)

    layout_utilities.addWidget(getbtninfo_frame, 4, 1, 4, 1)
    #...................................

    komodo_submit_btn.clicked.connect(lambda: panel1_functions.submit_pressed(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, listaddr_listbox_utilities, console_txt))

    getbalance_btn_utilities.clicked.connect(lambda: panel1_functions.btn_1(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt))
    genaddr_btn_utilities.clicked.connect(lambda: panel1_functions.btn_2(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, listaddr_listbox_utilities))
    sendtoaddr_btn_utilities.clicked.connect(lambda: panel1_functions.btn_3(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, senderaddr_txt, kmdamount_txt, extrainfo_txt))
    gettansinfo_btn_utilities.clicked.connect(lambda: panel1_functions.btn_4(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, btninfo_txt_utilities))
    valaddr_btn_utilities.clicked.connect(lambda: panel1_functions.btn_5(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, btninfo_txt_utilities))
    getnetinfo_btn_utilities.clicked.connect(lambda: panel1_functions.btn_6(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, btninfo_txt_utilities))
    addnode_btn_utilities.clicked.connect(lambda: panel1_functions.btn_7(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, btninfo_txt_utilities))
    getwalletinfo_btn_utilities.clicked.connect(lambda: panel1_functions.btn_8(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, btninfo_txt_utilities))

    getbalance_btn_utilities.mouseHover.connect(lambda: panel1_functions.hoverevent(0, btninfo_txt_utilities))
    genaddr_btn_utilities.mouseHover.connect(lambda: panel1_functions.hoverevent(1, btninfo_txt_utilities))
    sendtoaddr_btn_utilities.mouseHover.connect(lambda: panel1_functions.hoverevent(2, btninfo_txt_utilities))
    gettansinfo_btn_utilities.mouseHover.connect(lambda: panel1_functions.hoverevent(3, btninfo_txt_utilities))
    valaddr_btn_utilities.mouseHover.connect(lambda: panel1_functions.hoverevent(4, btninfo_txt_utilities))
    getnetinfo_btn_utilities.mouseHover.connect(lambda: panel1_functions.hoverevent(5, btninfo_txt_utilities))
    addnode_btn_utilities.mouseHover.connect(lambda: panel1_functions.hoverevent(6, btninfo_txt_utilities))
    getwalletinfo_btn_utilities.mouseHover.connect(lambda: panel1_functions.hoverevent(7, btninfo_txt_utilities))

    layout_komodo.addRow(layout_connect_frame, layout_utilities_frame)
    stack1.setLayout(layout_komodo)


class QHoverButton(QPushButton):
    mouseHover = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        self.setMouseTracking(True)

    def enterEvent(self, event):
        self.mouseHover.emit(True)

    def leaveEvent(self, event):
        self.mouseHover.emit(False)
