import os
import sys, random
from PyQt5.QtWidgets import QApplication, QWidget,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
from pathlib import Path
import shutil



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
        self.fullWay = QtWidgets.QLineEdit(self.centralwidget)
        self.fullWay.setGeometry(QtCore.QRect(50, 220, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(14)
        self.fullWay.setFont(font)
        self.fullWay.setStyleSheet("background-color:#f5f0e1;\n"
"border: 4px solid #1e3d59;\n"
"border-radius: 30;\n"
"color:#1e3d59\n"
"")
        self.fullWay.setAlignment(QtCore.Qt.AlignCenter)
        self.fullWay.setObjectName("fullWay")
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
        self.fullWay.setText(_translate("MainWindow", "INPUT FULL WAY"))
        self.CreateFirstCSV.setText(_translate("MainWindow", "1.Create the first csv file"))
        self.IMPORTdataset.setText(_translate("MainWindow", "2.Import in thr new dataset"))
        self.RANDOM.setText(_translate("MainWindow", "3.random dataset"))
        self.NEXTimg.setText(_translate("MainWindow", "output next img"))
        self.take.setText(_translate("MainWindow", "take the path"))
        self.EXIT.setText(_translate("MainWindow", "EXIT"))

def make_csv(name_csv: str) -> None:
    """Функция создает файл разрешения csv

    Args:
        name_csv (str): _название файла, который нужно создать_
    """
    with open(f"{name_csv}.csv", "w+", encoding="UTF-8", newline="") as file:
        csv_file = csv.writer(file, delimiter=";")
        csv_file.writerow(["Absolute path", "Relative path", "Class"])

def make_file_abstract(name_class: str, full_way: str, file_name: str) -> None:
    """Функция заполняет csv файл. В первый столбец полный путь файлов, второй столбец - путь

    Args:
        name_class (str)): _Название класса_
        full_way (str): _Полный путь к файлу_
        file_name (str): _имя файла разрешения csv_
    """
    full_way += name_class
    way = f"dataset/{name_class}/"
    folder = Path(full_way)
    if folder.is_dir():
        counter_files = len([1 for file in folder.iterdir()])  #
    with open(f"{file_name}.csv", "a", encoding="UTF-8", newline="") as file:
        csv_file = csv.writer(file, delimiter=";")
        for i in range(counter_files):
            csv_file.writerow([full_way + f"/{i}.jpg", way + f"{i}.jpg", name_class])

def porting(name_abstract: str, new_csv: str) -> None:
    """Функция импортируют файлы из собранного датасета в новый датасет. Файлы именуются по принципу "класс_Имяфайла.jpg"
        так же функция создает новый csv файл для нового датасета

    Args:
        name_abstract (str): имя csv из которого берем путь, имя и класс
        new_csv (str): имя csv файла в которой импортируем новый путь, имя и класс
    """
    try:
        os.mkdir("dataset")
    except:
        print("====ФАЙЛ ИМЕЕТСЯ====")
    with open(f"{name_abstract}.csv", newline="") as file:
        read = csv.DictReader(file, delimiter=";")
        with open(f"{new_csv}.csv", "a", encoding="UTF-8", newline="") as file1:
            csv_file = csv.writer(file1, delimiter=";")
            for row in read:
                FROM = row["Absolute path"]
                a = FROM.split("/")
                TO = f"dataset/{a[-2]}_{a[-1]}"
                shutil.copyfile(FROM, TO)
                name_class = row["Class"]

                fullWay = os.getcwd() + f"\dataset\{a[-2]}_{a[-1]}"
                Way = f"dataset\{a[-2]}_{a[-1]}"
                csv_file.writerow([fullWay, Way, name_class])

def random_name(file_abstract: str, new_abstract: str) -> None:  # 3 путкт
    """Функция импортируют файлы из собранного датасета в новый датасет с рандомным названием файла
        так же создается новый csv для навого датасета  для того чтобы осталась возможность определить принадлежность экземпляра к классу
    Args:
        file_abstract (str): имя csv из которого берем путь, имя и класс
        new_abstract (str):  имя csv файла в которой импортируем новый путь, имя и класс
    """
    b = []
    for i in range(0, 10001):
        b.append(i)
    c = random.sample(b, 2200)
    i = 0
    try:
        os.mkdir("dataset_random")
    except:
        print("====ФАЙЛ ИМЕЕТСЯ====")
    with open(f"{file_abstract}.csv", newline="") as file:
        read = csv.DictReader(file, delimiter=";")
        for row in read:
            FROM = row["Absolute path"]
            a = FROM.split("/")
            TO = f"dataset_random/{c[i]}.jpg"
            i += 1
            shutil.copyfile(FROM, TO)
            class_obj = row["Class"]
            with open(f"{new_abstract}.csv", "a", newline="") as file_new:
                csv_file = csv.writer(file_new, delimiter=";")
                slash1 = "\ "
                slash2 = "/"
                way = os.getcwd()
                counter = way.count(slash1[0])
                full_way = f"{way.replace(slash1[0],slash2,counter)}/{TO}"
                csv_file.writerow([full_way, TO, class_obj])


full_way=''
check_way=False
def push_Exit():
    sys.exit(app.exec_())
def push_takePath():
    global check_way
    global full_way
    full_way=ui.fullWay.text()+"/"
    if(os.path.exists(ui.fullWay.text()+"/CatIT")==False):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText("файлы не найдены!\nВведите путь еще раз")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
        check_way=False
    else:
        check_way=True
        print( full_way)

def script_1():
     global check_way
     if(check_way==True):
        make_csv("Dataset_script1")
        make_file_abstract("DogsIT", full_way,"Dataset_script1" )
        make_file_abstract("CatIT", full_way, "Dataset_script1")
     else:
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка!!!")
        msg.setText("Установлен неверный путь!!!\nВведите путь еще раз!!!")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
def script_2():
     global check_way
     if(check_way==True):
        make_csv("new_csv")
        porting("Dataset_script1","new_csv")
     else:
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка!!!")
        msg.setText("Хмммммм может быть уже введем нормальный путь или создадим первый csv файл ?!!!")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
def script_3():
    global check_way
    if(check_way==True):
        make_csv("random_csv")
        random_name("Dataset_script1","random_csv")
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка!!!")
        msg.setText("Установлен неверный путь!!!\nВведите путь еще раз!!!")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()


def Open_window_two():
    global Image
    Image = QtWidgets.QMainWindow()
    ui = Ui_Image()
    ui.setupUi(Image)
    Application.close()
    Image.show()

    def next_dog():
        pass
    def next_cat():
        pass

    def returnHub():
        Image.close()
        Application.show()

    ui.go_back.clicked.connect(returnHub)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Application = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Application )
    Application .show()
    app.setWindowIcon(QIcon('C:/Users/79093/Desktop/Application progra/laba3/GUI_lab/img/icon.ico'))
    ui.EXIT.clicked.connect(push_Exit)
    ui.take.clicked.connect(push_takePath)
    ui.CreateFirstCSV.clicked.connect(script_1)
    ui.IMPORTdataset.clicked.connect(script_2)
    ui.RANDOM.clicked.connect(script_3)
    ui.NEXTimg.clicked.connect(Open_window_two)
    sys.exit(app.exec_())
