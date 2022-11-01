import os
import sys, random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 749)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #f5f0e1")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-630, 0, 2031, 211))
        self.frame.setStyleSheet("background-color:#1e3d59")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.NAME = QtWidgets.QLabel(self.frame)
        self.NAME.setGeometry(QtCore.QRect(690, 10, 381, 51))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(10)
        self.NAME.setFont(font)
        self.NAME.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.NAME.setMouseTracking(False)
        self.NAME.setStyleSheet("color:#f5f0e1")
        self.NAME.setAlignment(QtCore.Qt.AlignCenter)
        self.NAME.setObjectName("NAME")
        self.logo = QtWidgets.QLabel(self.frame)
        self.logo.setGeometry(QtCore.QRect(630, 100, 111, 141))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(f"{os.getcwd()}/img/imgonline-com-ua-Resize-eaZg8IxsenvxUV.png"))
        self.logo.setObjectName("logo")
        self.logo_2 = QtWidgets.QLabel(self.frame)
        self.logo_2.setGeometry(QtCore.QRect(730, 120, 101, 101))
        self.logo_2.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.logo_2.setText("")
        self.logo_2.setPixmap(QtGui.QPixmap(f"{os.getcwd()}/img/imgonline-com-ua-Resize-eaZg8IxsenvxUV.png"))
        self.logo_2.setObjectName("logo_2")
        self.logo_3 = QtWidgets.QLabel(self.frame)
        self.logo_3.setGeometry(QtCore.QRect(830, 120, 101, 101))
        self.logo_3.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.logo_3.setText("")
        self.logo_3.setPixmap(QtGui.QPixmap(f"{os.getcwd()}/img/imgonline-com-ua-Resize-eaZg8IxsenvxUV.png"))
        self.logo_3.setObjectName("logo_3")
        self.logo_5 = QtWidgets.QLabel(self.frame)
        self.logo_5.setGeometry(QtCore.QRect(930, 120, 101, 101))
        self.logo_5.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.logo_5.setText("")
        self.logo_5.setPixmap(QtGui.QPixmap(f"{os.getcwd()}/img/imgonline-com-ua-Resize-eaZg8IxsenvxUV.png"))
        self.logo_5.setObjectName("logo_5")
        self.logo_4 = QtWidgets.QLabel(self.frame)
        self.logo_4.setGeometry(QtCore.QRect(1030, 120, 101, 101))
        self.logo_4.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.logo_4.setText("")
        self.logo_4.setPixmap(QtGui.QPixmap(f"{os.getcwd()}/img/imgonline-com-ua-Resize-eaZg8IxsenvxUV.png"))
        self.logo_4.setObjectName("logo_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 220, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:#f5f0e1;\n"
"border: 4px solid #1e3d59;\n"
"border-radius: 30;\n"
"color:#1e3d59\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.CreateFirstCSV = QtWidgets.QPushButton(self.centralwidget)
        self.CreateFirstCSV.setGeometry(QtCore.QRect(270, 400, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        self.CreateFirstCSV.setFont(font)
        self.CreateFirstCSV.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.CreateFirstCSV.setStyleSheet("QPushButton{\n"
"    background-color: #f5f0e1;\n"
"    border: 4px solid #1e3d59;\n"
"    border-radius: 30;\n"
"    color:#1e3d59\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #f5f0ef;\n"
"}\n"
"")
        self.CreateFirstCSV.setObjectName("CreateFirstCSV")
        self.IMPORTdataset = QtWidgets.QPushButton(self.centralwidget)
        self.IMPORTdataset.setGeometry(QtCore.QRect(20, 400, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        self.IMPORTdataset.setFont(font)
        self.IMPORTdataset.setStyleSheet("QPushButton{\n"
"    background-color: #f5f0e1;\n"
"    border: 4px solid #1e3d59;\n"
"    border-radius: 30;\n"
"    color:#1e3d59\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #f5f0ef;\n"
"}\n"
"")
        self.IMPORTdataset.setObjectName("IMPORTdataset")
        self.RANDOM = QtWidgets.QPushButton(self.centralwidget)
        self.RANDOM.setGeometry(QtCore.QRect(270, 500, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        self.RANDOM.setFont(font)
        self.RANDOM.setStyleSheet(
"QPushButton{\n"
"    background-color: #f5f0e1;\n"
"    border: 4px solid #1e3d59;\n"
"    border-radius: 30;\n"
"    color:#1e3d59\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #f5f0ef;\n"
"}\n"
"")
        self.RANDOM.setObjectName("RANDOM")
        self.NEXTimg = QtWidgets.QPushButton(self.centralwidget)
        self.NEXTimg.setGeometry(QtCore.QRect(20, 500, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        self.NEXTimg.setFont(font)
        self.NEXTimg.setStyleSheet("QPushButton{\n"
"    background-color: #f5f0e1;\n"
"    border: 4px solid #1e3d59;\n"
"    border-radius: 30;\n"
"    color:#1e3d59\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #f5f0ef;\n"
"}\n"
"")
        self.NEXTimg.setObjectName("NEXTimg")
        self.take = QtWidgets.QPushButton(self.centralwidget)
        self.take.setGeometry(QtCore.QRect(130, 290, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        self.take.setFont(font)
        self.take.setStyleSheet("QPushButton{\n"
"    background-color: #f5f0e1;\n"
"    border: 4px solid #1e3d59;\n"
"    border-radius: 25;\n"
"    color:#1e3d59\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #f5f0ef;\n"
"}\n"
"")
        self.take.setObjectName("take")
        self.EXIT = QtWidgets.QPushButton(self.centralwidget)
        self.EXIT.setGeometry(QtCore.QRect(140, 610, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(20)
        self.EXIT.setFont(font)
        self.EXIT.setStyleSheet("QPushButton{\n"
"    background-color: #f5f0e1;\n"
"    border: 4px solid #1e3d59;\n"
"    border-radius: 30;\n"
"    color:#1e3d59\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #f5f0ef;\n"
"}\n"
"")
        self.EXIT.setObjectName("EXIT")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NAME.setText(_translate("MainWindow", "The  coolest  app  in  the  world"))
        self.lineEdit.setText(_translate("MainWindow", "INPUT FULL WAY"))
        self.CreateFirstCSV.setText(_translate("MainWindow", "1.Create the first csv file"))
        self.IMPORTdataset.setText(_translate("MainWindow", "2.Import in thr new dataset"))
        self.RANDOM.setText(_translate("MainWindow", "3.random dataset"))
        self.NEXTimg.setText(_translate("MainWindow", "output next img"))
        self.take.setText(_translate("MainWindow", "take the path"))
        self.EXIT.setText(_translate("MainWindow", "EXIT"))

def push_Exit():
    sys.exit(app.exec_())
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Application = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Application )
    Application .show()
    app.setWindowIcon(QIcon('C:/Users/79093/Desktop/Application progra/laba3/GUI_lab/img/icon.ico'))
    
    ui.EXIT.clicked.connect(push_Exit)
    sys.exit(app.exec_())