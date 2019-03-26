from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QDialog, QWidget)

class mainWindow(QDialog):
    def __init__(self, parent = None):
        super(mainWindow, self).__init__(parent)
        pass

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())
