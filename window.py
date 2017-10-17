import sys
from PyQt5.QtWidgets import *
# (QWidget, QToolTip,
#     QPushButton, QApplication,QDesktopWidget,
#     QMainWindow, QAction, qApp, QGridLayout,
#     QHBoxLayout, QFrame, QSplitter)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.left = QListWidget()
        self.mid = QListWidget()
        self.right = QFrame()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        self.left.setFrameShape(QFrame.StyledPanel)    
        self.mid.setFrameShape(QFrame.StyledPanel)
        self.right.setFrameShape(QFrame.StyledPanel)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.left)
        splitter.addWidget(self.mid)
        splitter.addWidget(self.right)
        splitter.setStretchFactor(0,5);
        splitter.setStretchFactor(1,5);
        splitter.setStretchFactor(2,4);

        self.ResetLeft()

        self.setWindowTitle('PassWord')
        # set center
        self.resize(2050,1250)
        self.center()
        # set icon
        self.setWindowIcon(QIcon('icon.jpg'))
        hbox.addWidget(splitter)
        self.setLayout(hbox)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def ResetLeft(self):
        self.left.addItems(QIcon('icon.jpg'),'2')





def CreatWindow():
    app = QApplication(sys.argv)
    AppPassWord = App()

    sys.exit(app.exec_())

CreatWindow()



