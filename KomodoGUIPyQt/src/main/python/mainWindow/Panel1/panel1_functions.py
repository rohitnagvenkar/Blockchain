import subprocess


def inputValidation_1(hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt):
    check = True
    if hostname_txt.text() == "":
        hostname_txt.setStyleSheet("border: 2px solid red;")
        check = False
    else:
        hostname_txt.setStyleSheet("border:1px solid rgb(0, 255, 0)")

    if hostport_txt.text() == "":
        hostport_txt.setStyleSheet("border: 2px solid red;")
        check = False
    else:
        hostport_txt.setStyleSheet("border:1px solid rgb(0, 255, 0)")

    if hostusername_txt.text() == "":
        hostusername_txt.setStyleSheet("border: 2px solid red;")
        check = False
    else:
        hostusername_txt.setStyleSheet("border:1px solid rgb(0, 255, 0)")

    if hostpassword_txt.text() == "":
        hostpassword_txt.setStyleSheet("border: 2px solid red;")
        check = False
    else:
        hostpassword_txt.setStyleSheet("border:1px solid rgb(0, 255, 0)")

    return check


def inputValidation_2(hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt):
    check = True
    if hostname_txt.text() == "":
        hostname_txt.setStyleSheet("border: 2px solid red;")
        check = False
    if hostport_txt.text() == "":
        hostport_txt.setStyleSheet("border: 2px solid red;")
        check = False
    if hostusername_txt.text() == "":
        hostusername_txt.setStyleSheet("border: 2px solid red;")
        check = False
    if hostpassword_txt.text() == "":
        hostpassword_txt.setStyleSheet("border: 2px solid red;")
        check = False
    return check
#password12345678
#rohit


def submit_pressed(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, listaddr_listbox_utilities, console_txt):
    if inputValidation_1(hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt):
        username = hostusername_txt.text()
        password = hostpassword_txt.text()
        host = 'http://' + hostname_txt.text() + ':' + hostport_txt.text() + '/'
        command = '''curl -vs --user ''' + username + ':' + password + ''' --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getbalance", "params": ["", 6] }' -H 'content-type: text/plain;' ''' + host
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        print(out)
        print(err)
        console_txt.append(str(err))


def hoverevent(btnID, txt):
    if btnID == 0:
        textstr = "Get Balance: \n\n" \
                  "This method returns the server's total available balance."
        txt.setText(textstr)
    elif btnID == 1:
        textstr = "Generate Address: \n\n" \
                  "This method returns a new address for receiving payments."
        txt.setText(textstr)
    elif btnID == 2:
        textstr = "Send To Address: \n\n" \
                  "This method sends an amount to a given address. " \
                  "The amount is real and is rounded to the nearest 0.00000001."
        txt.setText(textstr)
    elif btnID == 3:
        textstr = "Get Transaction Info: \n\n" \
                  "This method queries detailed information about transaction txid. " \
                  "This command applies only to txid's that are in the user's local wallet."
        txt.setText(textstr)
    elif btnID == 4:
        textstr = "Validate Address: \n\n" \
                  "This method returns information about the given address."
        txt.setText(textstr)
    elif btnID == 5:
        textstr = "Get Network Info: \n\n" \
                  "This method returns returns an object containing various state info regarding P2P networking."
        txt.setText(textstr)
    elif btnID == 6:
        textstr = "Add new Node: \n\n" \
                  "This method attempts to adds a node from the addnode list, " \
                  "or to make a single attempt to connect to a node."
        txt.setText(textstr)
    elif btnID == 7:
        textstr = "Get Wallet Info: \n\n" \
                  "This method returns an object containing various information about the wallet state."
        txt.setText(textstr)
    else:
        textstr = ""
        txt.setText(textstr)


def btn_1(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, btninfo_txt_utilities):
    print("btn_1")


def btn_2(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, btninfo_txt_utilities):
    print("btn_2")


def btn_3(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, btninfo_txt_utilities):
    print("btn_3")


def btn_4(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, btninfo_txt_utilities):
    print("btn_4")


def btn_5(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, btninfo_txt_utilities):
    print("btn_5")


def btn_6(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, btninfo_txt_utilities):
    print("btn_6")


def btn_7(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, btninfo_txt_utilities):
    print("btn_7")


def btn_8(self, hostname_txt, hostport_txt, hostusername_txt, hostpassword_txt, btninfo_txt_utilities):
    print("btn_7")