# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(10, 10, 10);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(170, 0, 0);")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.btnmenu1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnmenu1.setGeometry(QtCore.QRect(440, 164, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnmenu1.setFont(font)
        self.btnmenu1.setStyleSheet("background-color: rgb(77, 63, 75);")
        self.btnmenu1.setObjectName("btnmenu1")
        self.btnmenu2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnmenu2.setGeometry(QtCore.QRect(440, 226, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnmenu2.setFont(font)
        self.btnmenu2.setStyleSheet("background-color: rgb(77, 63, 75);")
        self.btnmenu2.setObjectName("btnmenu2")
        self.btnmenu3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnmenu3.setGeometry(QtCore.QRect(440, 288, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnmenu3.setFont(font)
        self.btnmenu3.setStyleSheet("background-color: rgb(77, 63, 75);")
        self.btnmenu3.setObjectName("btnmenu3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 460, 361, 51))
        self.label_2.setObjectName("label_2")
        self.imgLabel = QtWidgets.QLabel(self.centralwidget)
        self.imgLabel.setGeometry(QtCore.QRect(80, 160, 311, 231))
        self.imgLabel.setStyleSheet("background-image: url(:/prefijoNuevo/menu.jpg);")
        self.imgLabel.setText("")
        self.imgLabel.setPixmap(QtGui.QPixmap(":/prefijoNuevo/menu.jpg"))
        self.imgLabel.setScaledContents(True)
        self.imgLabel.setObjectName("imgLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label.setText(_translate("MainWindow", "BIENVENIDO AL LECTOR DE ASTEROIDES DE LA NASA"))
        self.btnmenu1.setText(_translate("MainWindow", "Capturar Información API NASA"))
        self.btnmenu2.setText(_translate("MainWindow", "Información Guardada"))
        self.btnmenu3.setText(_translate("MainWindow", "Imagenes API NASA"))
        self.label_2.setText(_translate("MainWindow", "Selección"))

import imgs1_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

