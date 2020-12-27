import sys
import requests
from interface_ui import *
from interface_ui2 import *
from interface_ui3 import *
from interface_ui4 import *
import urllib
import pymysql
from PyQt5.QtGui import QPixmap, QIcon



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.label_2.setText("Hola mundo")
        self.btnmenu1.clicked.connect(self.opcion1)
        self.btnmenu2.clicked.connect(self.opcion2)
        self.btnmenu3.clicked.connect(self.opcion3)
    
    def opcion1(self):
        self.window1 = window1()
        self.hide()
        self.window1.show()
    
    def opcion2(self):
        self.window2 = window2()
        self.hide()
        self.window2.show()
    
    def opcion3(self):
        self.window3 = window3()
        self.hide()
        self.window3.show()


    def actualizar(self):
        pass

class window1(QtWidgets.QMainWindow, Ui_MainWindow2):

    def __init__(self, *args, **kwargs):
        self.r = requests.get('https://api.nasa.gov/neo/rest/v1/feed?api_key=ooyOyfc1LD91FDtXEpzSscSOH8m6Iaq0QDaCFgX7')
        #self.r ={"maldita":"Sea"}
        self.conexion = False
        self.respuesta=self.r.json()
        self.indice = 0
        self.limite = 1
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.resp_id=[]
        self.resp_name=[]
        self.resp_hazardous=[]
        self.diameter_min=[]
        self.diameter_max=[]
        self.setupUi(self)
        self.btnconsulta.clicked.connect(self.realizar_conexion)
        self.pushButton_3.clicked.connect(self.guardar)
        self.pushButton.clicked.connect(self.aumentar_indice)
        self.pushButton_2.clicked.connect(self.disminuir_indice)
        self.pushButton_4.clicked.connect(self.volvermenu)
    
    def guardar(self):
        if self.conexion:
            connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='proyectofinal',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            
            try:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO `asteroides` (`idnasa`,`name`,`diameter_min`, `diameter_max`, `hazardous`) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql, (self.resp_id[self.indice], self.resp_name[self.indice], str(self.diameter_min[self.indice]), str(self.diameter_max[self.indice]), 'True'))
                connection.commit()
            finally:
                connection.close()

    def aumentar_indice(self):
        if self.indice < self.limite:
            self.indice+=1
            self.actualiza()
    
    def disminuir_indice(self):
        if self.indice > 0:
            self.indice-=1
            self.actualiza()

    def volvermenu(self):
        self.window1 = MainWindow()
        self.hide()
        self.window1.show()


    def actualiza(self):
        self.resultadoId.setText(self.resp_id[self.indice])
        self.resultadoName.setText(self.resp_name[self.indice])
        self.resultadomin.setText(str(self.diameter_min[self.indice]))
        self.resultadomax.setText(str(self.diameter_max[self.indice]))
        self.resultadohar.setText(format(self.resp_hazardous[self.indice]))


    def realizar_conexion(self):
        try:
            asteroides = self.respuesta["near_earth_objects"]
        except:
            print("Ha ocurrrido un error con la conexion")
        else:
            print("Conectado")
            self.conexion = True
            self.resp_keys= dict.keys(asteroides)
            for self.resp_keys in asteroides:
                r2 = asteroides[self.resp_keys]
                k=0
                kfinal = len(r2)
                while k<kfinal:
                    asteroide = r2[k]
                    self.resp_id.append(asteroide['id'])
                    self.resp_name.append(asteroide['name'])
                    self.diameter=asteroide['estimated_diameter']
                    self.kilometers=self.diameter['kilometers']
                    self.diameter_min.append(self.kilometers['estimated_diameter_min'])
                    self.diameter_max.append(self.kilometers['estimated_diameter_max'])
                    self.resp_hazardous.append(asteroide["is_potentially_hazardous_asteroid"])
                    k+=1
                
            self.label_8.setStyleSheet("background-color: rgb(91, 246, 105);")
            self.limite = len(self.resp_id)
            self.limite-=1
            self.resultadoId.setText(self.resp_id[0])
            self.resultadoName.setText(self.resp_name[0])
            self.resultadomin.setText(str(self.diameter_min[0]))
            self.resultadomax.setText(str(self.diameter_max[0]))
            self.resultadohar.setText(format(self.resp_hazardous[0]))
            
            #long = 0
            #lim1 = len(self.resp_id)

            # while long < lim1:
            #     print(f"ID del asteroide: {self.resp_id[long]}")
            #     print(f"Nombre del asteroide: {self.resp_name[long]}")
            #     print(f"Diametro min (Km): {self.diameter_min[long]}")
            #     print(f"Diametro max (Km): {self.diameter_max[long]}")
            #     print(f"Potencialmente Peligroso: {self.resp_hazardous[long]}")
            #     long+=1
            

 
class window2(QtWidgets.QMainWindow, Ui_MainWindow3):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.resp_id=[]
        self.resp_name=[]
        self.resp_hazardous=[]
        self.diameter_min=[]
        self.diameter_max=[]
        self.bandera_conexion = False
        self.indice = 0
        self.limite = 1
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='proyectofinal',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `asteroides`"
                cursor.execute(sql, )
                row = cursor.fetchone()
                while row is not None:
                    self.resp_id.append(row['idnasa'])
                    self.resp_name.append(row['name'])
                    self.diameter_min.append(row['diameter_min'])
                    self.diameter_max.append(row['diameter_max'])
                    self.resp_hazardous.append(row['hazardous'])
                    row = cursor.fetchone()
            connection.commit()
        finally:
            self.bandera_conexion = True
            connection.close()
        self.setupUi(self)
        self.btnconsulta.clicked.connect(self.actualizar)
        self.pushButton.clicked.connect(self.aumentar_indice)
        self.pushButton_2.clicked.connect(self.disminuir_indice)
        self.pushButton_4.clicked.connect(self.volvermenu)
        #comenzar aca
    
    def aumentar_indice(self):
        if self.indice < self.limite:
            self.indice+=1
            self.actualiza()
    
    def disminuir_indice(self):
        if self.indice > 0:
            self.indice-=1
            self.actualiza()
    def actualiza(self):
        self.resultadoId.setText(self.resp_id[self.indice])
        self.resultadoName.setText(self.resp_name[self.indice])
        self.resultadomin.setText(str(self.diameter_min[self.indice]))
        self.resultadomax.setText(str(self.diameter_max[self.indice]))
        self.resultadohar.setText(format(self.resp_hazardous[self.indice]))
    
    def volvermenu(self):
        self.window1 = MainWindow()
        self.hide()
        self.window1.show()

    def actualizar(self):
        if self.bandera_conexion:
            print("Conectado")
            self.label_8.setStyleSheet("background-color: rgb(91, 246, 105);")
            self.limite = len(self.resp_id)
            self.limite-=1
            self.resultadoId.setText(self.resp_id[0])
            self.resultadoName.setText(self.resp_name[0])
            self.resultadomin.setText(str(self.diameter_min[0]))
            self.resultadomax.setText(str(self.diameter_max[0]))
            self.resultadohar.setText(format(self.resp_hazardous[0]))

class window3(QtWidgets.QMainWindow, Ui_MainWindow4):

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