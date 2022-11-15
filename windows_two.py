

class Ui_Image(object):
    def setupUi(self, Image):
        Image.setObjectName("Image")
        Image.resize(832, 734)
        self.centralwidget = QtWidgets.QWidget(Image)
        self.centralwidget.setStyleSheet("    background-color: #f5f0e1;")
        self.centralwidget.setObjectName("centralwidget")
        self.next_dog = QtWidgets.QPushButton(self.centralwidget)
        self.next_dog.setGeometry(QtCore.QRect(20, 570, 301, 81))
        self.next_dog.setStyleSheet("QPushButton{\n"
"    background-color: #f5f0e1;\n"
"    border: 4px solid #1e3d59;\n"
"    border-radius: 30;\n"
"    color:#1e3d59\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #f5f0ef;\n"
"}\n"
"")
        self.next_dog.setObjectName("next_dog")
        self.next_cat = QtWidgets.QPushButton(self.centralwidget)
        self.next_cat.setGeometry(QtCore.QRect(500, 570, 301, 81))
        self.next_cat.setStyleSheet("QPushButton{\n"
"    background-color: #f5f0e1;\n"
"    border: 4px solid #1e3d59;\n"
"    border-radius: 30;\n"
"    color:#1e3d59\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #f5f0ef;\n"
"}\n"
"")
        self.next_cat.setObjectName("next_cat")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-490, 0, 2031, 161))
        self.frame.setStyleSheet("background-color:#1e3d59\n"
"")
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
        self.go_back = QtWidgets.QPushButton(self.frame)
        self.go_back.setGeometry(QtCore.QRect(500, 10, 61, 61))
        self.go_back.setStyleSheet("QPushButton{\n"
"    background-color: #f5f0e1;\n"
"    border: 4px solid #1e3d59;\n"
"    border-radius: 30;\n"
"    color:#1e3d59\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #f5f0ef;\n"
"}\n"
"")
        self.go_back.setObjectName("go_back")
        self.Dogimg = QtWidgets.QLabel(self.centralwidget)
        self.Dogimg.setGeometry(QtCore.QRect(50, 210, 321, 271))
        self.Dogimg.setText("")
        self.Dogimg.setObjectName("Dogimg")
        self.Catimg = QtWidgets.QLabel(self.centralwidget)
        self.Catimg.setGeometry(QtCore.QRect(470, 210, 321, 271))
        self.Catimg.setText("")
        self.Catimg.setObjectName("Catimg")
        Image.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Image)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 26))
        self.menubar.setObjectName("menubar")
        Image.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Image)
        self.statusbar.setObjectName("statusbar")
        Image.setStatusBar(self.statusbar)

        self.retranslateUi(Image)
        QtCore.QMetaObject.connectSlotsByName(Image)

    def retranslateUi(self, Image):
        _translate = QtCore.QCoreApplication.translate
        Image.setWindowTitle(_translate("Image", "MainWindow"))
        self.next_dog.setText(_translate("Image", "NEXT DOG"))
        self.next_cat.setText(_translate("Image", "NEXT CAT"))
        self.NAME.setText(_translate("Image", "The  coolest  app  in  the  world"))
        self.go_back.setText(_translate("Image", "BACK"))


