from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, Qt, QTimer

class WindowMain(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(WindowMain, self).__init__(parent)
        self.setWindowTitle("fpena2")
        self.InitwelcomeScreen()
    
    def InitwelcomeScreen(self):
        self.mainWidget = QtWidgets.QWidget()               
        mainWidgetlayout = QtWidgets.QVBoxLayout(self.mainWidget)

        welcomeScreen = QtWidgets.QLabel(self)
        photo = QtGui.QPixmap("logo.png")
        welcomeScreen.setPixmap(photo)
        self.setFixedSize(WIDTH, HEIGHT)

        #might have to add these to the mainwidgetlayout
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.move(360,535)
        self.buttonLogin.clicked.connect(self.getLoginWindow)
        self.buttonCreateAcc = QtWidgets.QPushButton('Create Account', self)
        self.buttonCreateAcc.move(360,570)
        self.buttonCreateAcc.clicked.connect(self.getCreateAccountWindow)
        
        mainWidgetlayout.addWidget(welcomeScreen)
        self.show()

    def getCreateAccountWindow(self):
       self.obj = windowCreateAccount()


    def getLoginWindow(self):
        pass

class windowCreateAccount(QtWidgets.QWidget):
    def __init__(self, parent= None):
        super(windowCreateAccount, self).__init__(parent)
        self.setWindowTitle("Create Account")
        
        # Accessed by multiple functions
        self.nameID = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.comboBox = QtWidgets.QComboBox()

        self.InitCreateAccount()

    def InitCreateAccount(self):
        organization = ["New Jersey", "New York", "California", "Florida"]

        mainWidgetlayout = QtWidgets.QGridLayout()  
        mainWidgetlayout.addWidget(QtWidgets.QLabel("ID: "), 1 , 0)
        mainWidgetlayout.addWidget(self.nameID, 1,1)
        mainWidgetlayout.addWidget(QtWidgets.QLabel("Password: "), 2 , 0)
        mainWidgetlayout.addWidget(self.password, 2,1)
        mainWidgetlayout.addWidget(QtWidgets.QLabel("Organization: "), 3 , 0)
        
        self.comboBox.addItems(organization)
        mainWidgetlayout.addWidget(self.comboBox, 3, 1)

        buttonSubmit = QtWidgets.QPushButton('Submit', self)
        buttonSubmit.clicked.connect(self.submitHandler)
        buttonCancel = QtWidgets.QPushButton('Cancel', self)
        buttonCancel.clicked.connect(self.close)
        mainWidgetlayout.addWidget(buttonCancel, 4, 0)
        mainWidgetlayout.addWidget(buttonSubmit, 4, 1)
        
        self.setLayout(mainWidgetlayout)
        self.show()

    def submitHandler(self):
        print(self.nameID.text())
        print(self.password.text())
        print(str(self.comboBox.currentText()))


if __name__ == '__main__':
    import sys
    HEIGHT = 600
    WIDTH = 800
    app = QtWidgets.QApplication(sys.argv)
    main = WindowMain()
    main.show()
    sys.exit(app.exec_())

    # if login.exec_() == QtWidgets.QDialog.Accepted:
    #     window = Window()
    #     window.show()
    #     sys.exit(app.exec_())

  
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