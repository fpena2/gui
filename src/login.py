import os
from PyQt5 import QtWidgets, QtGui, QtCore
from accountHandle import userTools


class WindowMain(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(WindowMain, self).__init__(parent)
        self.setWindowTitle("fpena2")
        self.InitwelcomeScreen()

    def InitwelcomeScreen(self):
        mainWidgetlayout = QtWidgets.QVBoxLayout(self)

        welcomeScreen = QtWidgets.QLabel(self)
        logoPath = os.path.join(os.path.dirname(
            os.getcwd()), "media", "logo.png")
        photo = QtGui.QPixmap(logoPath)
        welcomeScreen.setPixmap(photo)
        self.setFixedSize(WIDTH, HEIGHT)

        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.move(360, 535)
        self.buttonLogin.clicked.connect(self.getLoginWindow)
        self.buttonCreateAcc = QtWidgets.QPushButton('Create Account', self)
        self.buttonCreateAcc.move(360, 570)
        self.buttonCreateAcc.clicked.connect(self.getCreateAccountWindow)

        mainWidgetlayout.addWidget(welcomeScreen)

    def getCreateAccountWindow(self):
        self.obj = windowCreateAccount()

    def getLoginWindow(self):
        self.obj = windowLogin()


class windowCreateAccount(QtWidgets.QDialog):
    def __init__(self, parent=None):       
        super(windowCreateAccount, self).__init__(parent)
        self.setWindowTitle("Create Account")
        # Prevents manipulation of WindowMain 
        self.setModal(True)

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
        mainWidgetlayout.addWidget(QtWidgets.QLabel("ID: "), 1, 0)
        mainWidgetlayout.addWidget(self.nameID, 1, 1)
        mainWidgetlayout.addWidget(QtWidgets.QLabel("Password: "), 2, 0)
        mainWidgetlayout.addWidget(self.password, 2, 1)
        mainWidgetlayout.addWidget(QtWidgets.QLabel("Organization: "), 3, 0)

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
        dataPacket = (self.nameID.text(), self.password.text(),
                      str(self.comboBox.currentText()))

        handle = userTools()
        # returns flag if user already exist
        newUser = handle.pushNewUser(dataPacket)
        if newUser == 0:
            QtWidgets.QMessageBox.warning(
                self, "Attention", "This user already exist.")
        else:
            QtWidgets.QMessageBox.warning(
                self, "Success", "New user has been created.")
            self.close()


class windowLogin(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(windowLogin, self).__init__(parent)
        self.setWindowTitle("Log In")
        # Prevents manipulation of WindowMain 
        self.setModal(True)

        # Accessed by multiple functions
        self.nameID = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.InitLogin()

    def InitLogin(self):
        mainWidgetlayout = QtWidgets.QGridLayout()
        mainWidgetlayout.addWidget(QtWidgets.QLabel("ID: "), 1, 0)
        mainWidgetlayout.addWidget(self.nameID, 1, 1)
        mainWidgetlayout.addWidget(QtWidgets.QLabel("Password: "), 2, 0)
        mainWidgetlayout.addWidget(self.password, 2, 1)
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
            QtWidgets.QMessageBox.warning(
                self, "Attention", "Wrong user name or password")
        else:
            self.close()
            # Go to another main window
            self.obj = windowFinal()


class windowFinal(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(windowFinal, self).__init__(parent)
        # could make a closeWindow() func and call self.close
        main.hide()  # hides the main window
        self.setWindowTitle("We did it!")
        finalScreen = QtWidgets.QLabel(self)
        successPath = os.path.join(os.path.dirname(
            os.getcwd()), "media", "success.jpg")
        photo = QtGui.QPixmap(successPath)
        finalScreen.setPixmap(photo)
        self.resize(photo.width(), photo.height())
        self.show()


if __name__ == '__main__':
    import sys
    HEIGHT = 600
    WIDTH = 800
    # GTK 3 will force a warning:
    # (QApplication: invalid style override passed, ignoring it.)
    QtWidgets.QApplication.setDesktopSettingsAware(False)
    # This flag does not fix the issue under Pantheon (eOS)
    app = QtWidgets.QApplication(sys.argv)
    # app.setQuitOnLastWindowClosed(True)
    main = WindowMain()
    main.show()
    sys.exit(app.exec_())
