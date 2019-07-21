from PyQt5.QtWidgets import *
import sys
from src.main.python import login, register
from src.main.python.mainWindow import mainWindow


#for facebook google integration
#import webbrowser
#webbrowser.open('http://stackoverflow.com')


class LogicBoard:
    def __init__(self):
        pass

    def show_login(self):
        self.login = login.Login()
        self.login.switch_window.connect(self.show_choice)
        self.login.show()

    def show_choice(self, text, user):
        if text == "register":
            self.show_register()
            self.login.close()
        elif text == "login":
            self.show_login()
            self.register.close()
        elif text == "mainWindow":
            self.register.close()
            self.show_main(user)
        else:
            self.show_main(user)

    def show_register(self):
        self.register = register.Register()
        self.register.switch_window.connect(self.show_choice)
        self.login.close()
        self.register.show()

    def show_main(self, user):
        self.window = mainWindow.MainWindow(user)
        self.login.close()
        self.window.show()




def main():
    app = QApplication(sys.argv)  # 1. Instantiate ApplicationContext
    lb = LogicBoard()
    lb.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
