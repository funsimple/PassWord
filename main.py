import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication,QDesktopWidget,
    QMainWindow, QAction, qApp)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PassWord')
        # set center
        self.resize(2000,1500)
        self.center()
        # set icon
        self.setWindowIcon(QIcon('icon.jpg'))
        # button add password
        btnAdd = QPushButton('添加密码',self)
        btnAdd.move(1000,750)
        # btnAdd.clicked.connect(QCoreApplication.instance().quit)
        # statueBar
        self.statusBar().showMessage('Ready')

        #toolbar
        exitAction = QAction(QIcon('icon.jpg'),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('MainToolBar')
        self.toolbar.addAction(exitAction)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(exitAction)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    AppPassWord = App()

    sys.exit(app.exec_())