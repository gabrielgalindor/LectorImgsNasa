import sys
import requests
from interface_ui import *
from interface_ui2 import *
from interface_ui3 import *
from interface_ui4 import *
import pymysql
import json
import urllib
from PyQt5.QtGui import QPixmap, QIcon



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow4):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        url = 'https://images-assets.nasa.gov/image/PIA19379/PIA19379~thumb.jpg' 
        data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.label.setPixmap(pixmap)
        self.listaImgs =[]
        self.indice = 0
        self.limite = 1
        self.pushButton_2.clicked.connect(self.disminuir)
        self.pushButton_3.clicked.connect(self.aumentar)
        try:
            self.r = requests.get('https://images-api.nasa.gov/search?q=asteroid')
            a1=self.r.json()
            a2=a1["collection"]
            a3=a2["items"]
            for a4 in a3:
                a5=a4["links"]
                a6=a5[0]
                if "jpg" in a6["href"]:
                    if "video" not in a6["href"]:
                        self.listaImgs.append(a6["href"]) 

            #print(alphapha)
        except:
            print("Ha ocurrido un error")
            self.listaImgs.append("https://images-assets.nasa.gov/image/PIA19379/PIA19379~thumb.jpg")
        finally:
            print("Vidal")
            self.limite = len(self.listaImgs)
            self.limite-=1


        #self.label.setStyleSheet("background-image: url();")
        #self.label.setPixmap(QtGui.QPixmap(":/prefijoNuevo/noimage.png"))
    
    def aumentar(self):
        if self.indice < self.limite:
            self.indice+=1
            url1 = self.listaImgs[self.indice]
            data = urllib.request.urlopen(url1).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            self.label.setPixmap(pixmap)
    
    def disminuir(self):
        if self.indice > 0:
            self.indice-=1
            url1 = self.listaImgs[self.indice]
            data = urllib.request.urlopen(url1).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            self.label.setPixmap(pixmap)
    

    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()