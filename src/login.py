import os
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, Qt, QTimer
from accountHandle import userTools

class WindowMain(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WindowMain, self).__init__(parent)
        self.setWindowTitle("fpena2")
        self.InitwelcomeScreen()
    
    def InitwelcomeScreen(self):
        mainWidgetlayout = QtWidgets.QVBoxLayout(self)

        welcomeScreen = QtWidgets.QLabel(self)
        logoPath = os.path.join(os.path.dirname(os.getcwd()), "media", "logo.png")
        photo = QtGui.QPixmap(logoPath)
        welcomeScreen.setPixmap(photo)
        self.setFixedSize(WIDTH, HEIGHT)

        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.move(360,535)
        self.buttonLogin.clicked.connect(self.getLoginWindow)
        self.buttonCreateAcc = QtWidgets.QPushButton('Create Account', self)
        self.buttonCreateAcc.move(360,570)
        self.buttonCreateAcc.clicked.connect(self.getCreateAccountWindow)
        
        mainWidgetlayout.addWidget(welcomeScreen)
 
    def getCreateAccountWindow(self):
       self.obj = windowCreateAccount()

    def getLoginWindow(self):
        self.obj = windowLogin()

class windowCreateAccount(QtWidgets.QWidget):
    def __init__(self, parent= None):
        super(windowCreateAccount, self).__init__(parent)
        self.setWindowTitle("Create Account")
        
        # Accessed by multiple functions
        self.nameID = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        # Hides password field
        self.password.setEchoMode(QtWidgets.QLineEdit.Password) 
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
        dataPacket = (self.nameID.text(), self.password.text(),str(self.comboBox.currentText()))
        handle = userTools()
        # returns flag if user already exist
        newUser = handle.pushNewUser(dataPacket)
        if newUser == 0: 
            QtWidgets.QMessageBox.warning(self, "Attention", "This user already exist.")

class windowLogin(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(windowLogin, self).__init__(parent)
        self.setWindowTitle("Log In")
        # Accessed by multiple functions
        self.nameID = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.InitLogin()
    
    def InitLogin(self):
        mainWidgetlayout = QtWidgets.QGridLayout()  
        mainWidgetlayout.addWidget(QtWidgets.QLabel("ID: "), 1 , 0)
        mainWidgetlayout.addWidget(self.nameID, 1,1)
        mainWidgetlayout.addWidget(QtWidgets.QLabel("Password: "), 2 , 0)
        mainWidgetlayout.addWidget(self.password, 2,1)
        buttonSubmit = QtWidgets.QPushButton('Submit', self)
        buttonSubmit.clicked.connect(self.submitHandler)
        buttonCancel = QtWidgets.QPushButton('Cancel', self)
        buttonCancel.clicked.connect(self.close)
        mainWidgetlayout.addWidget(buttonCancel, 4, 0)
        mainWidgetlayout.addWidget(buttonSubmit, 4, 1)
        self.setLayout(mainWidgetlayout)
        self.show()
    
    def submitHandler(self):
        dataPacket = (self.nameID.text(), self.password.text())
        handle = userTools()
        loginStatus = handle.loginUser(dataPacket)
        if loginStatus != 1:
            QtWidgets.QMessageBox.warning(self, "Attention", "Wrong user name or password")
        else: 
            # Go to another main window 
            self.close()

        

if __name__ == '__main__':
    import sys
    HEIGHT = 600
    WIDTH = 800
    # GTK 3 will force a warning:
    # (QApplication: invalid style override passed, ignoring it.)
    QtWidgets.QApplication.setDesktopSettingsAware(False)
    # This flag does not fix the issue under Pantheon (eOS)
    app = QtWidgets.QApplication(sys.argv)
    main = WindowMain()
    main.show()
    sys.exit(app.exec_())



    # if login.exec_() == QtWidgets.QDialog.Accepted:
    #     window = Window()
    #     window.show()
    #     sys.exit(app.exec_())

    # def handleLogin(self):
    #     if (self.Name.text() == 'foo' and
    #             self.Password.text() == 'bar'):
    #         self.accept()
    #     else:
    #         QtWidgets.QMessageBox.warning(
    #             self, 'Error', 'Bad user or password')
