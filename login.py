from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore


class Login(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle("fpena2")
        self.welcomeScreen()
    
    def welcomeScreen(self):
        
        self.mainWidget = QtWidgets.QWidget()               
        self.setCentralWidget(self.mainWidget)    
        mainWidgetlayout = QtWidgets.QVBoxLayout(self.mainWidget)


        welcomeScreen = QtWidgets.QLabel(self)
        photo = QtGui.QPixmap("logo.png")
        welcomeScreen.setPixmap(photo)
        self.setFixedSize(WIDTH, HEIGHT)

        #might have to add these to the mainwidgetlayout
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.move(360,535)
        self.buttonLogin.clicked.connect(self.screenLogin)
        self.buttonCreateAcc = QtWidgets.QPushButton('Create Account', self)
        self.buttonCreateAcc.move(360,570)
        self.buttonCreateAcc.clicked.connect(self.screenCreateAcc)

        mainWidgetlayout.addWidget(welcomeScreen)
        self.show()

    def screenCreateAcc(self):
        pass

    def screenLogin(self):
        self.Name = QtWidgets.QLineEdit(self)
        self.Password = QtWidgets.QLineEdit(self)
        pass
  
'''
    # def loginScreen(self):

    #     #self.buttonLogin = QtWidgets.QPushButton('Login', self)
    #     #self.buttonLogin.clicked.connect(self.handleLogin)
    #     self.loginBox = QtWidgets.QGroupBox("Group 1")
    #     Box = QtWidgets.QVBoxLayout(self)
    #     Box.addWidget(QtWidgets.QLabel("Name"))
    #     Box.addWidget(self.Name)
    #     Box.addWidget(QtWidgets.QLabel("Password"))
    #     Box.addWidget(self.Password)
    #     Box.addWidget(QtWidgets.QLabel(""))
    #     Box.addWidget(self.buttonLogin)
    #     self.loginBox.setLayout(Box)

    #     loginLayout = QtWidgets.QGridLayout()
    #     loginLayout.addWidget(self.loginBox, 1, 0)
    #     self.setLayout(loginLayout)

    # def handleLogin(self):
    #     if (self.Name.text() == 'foo' and
    #             self.Password.text() == 'bar'):
    #         self.accept()
    #     else:
    #         QtWidgets.QMessageBox.warning(
    #             self, 'Error', 'Bad user or password')
    
    # def handleCreateAcc(self): 
    #     print("create account")

'''

class Window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

if __name__ == '__main__':
    import sys
    HEIGHT = 600
    WIDTH = 800
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())

    # if login.exec_() == QtWidgets.QDialog.Accepted:
    #     window = Window()
    #     window.show()
    #     sys.exit(app.exec_())
