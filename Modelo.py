import mysql.connector
from Producto import Producto

class Conectar:
    def __init__(self, host, user, password, database, port):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'wondershared98'
        self.database = 'bd_grupo4'
        self.connection = None
        self.port = 3306

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        if self.connection.is_connected():
            print("Conexión exitosa a la base de datos.")
        else:
            print("Error al conectar a la base de datos.")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Desconexión exitosa de la base de datos.")

    def insert_data(self, table, data):
        query = "INSERT INTO {} VALUES {}".format(table, data)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("Datos insertados correctamente.")

    def select_data(self, table):
        query = "SELECT * FROM {}".format(table)
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
    def delete_data(self, table):
        query = "DELETE * FROM {}".format(table)
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
    def update_data(self, table):
        query = "UPDATE * FROM {}".format(table)
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

db = Conectar('localhost', 'root', 'wondershared98', 'bd_grupo4', 'port')


class Producto():
    ID_Producto =0,
    Nombre_Producto = "",
    Stock =0,
    Precio = 0,
    Unidad_de_medida = "",
    ID_Receta = 0

    def __init__(self,iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta):
        self.ID_Producto = iD_Producto
        self.Nombre_Producto =nombre_Producto
        self.Stock = stock
        self.Precio = precio
        self.Unidad_de_medida=unidad_de_medida
        self.ID_Receta =iD_Receta
    
    def getiD_Producto(self):
        return self.iD_Producto
    def getnombre_Producto(self):
        return self.nombre_Producto
    def getstock(self):
        return self.stock
    def getprecio(self):
        return self.precio
    def getunidad_de_medida(self):
        return self.unidad_de_medida
    def getiD_Receta(self):
        return self.iD_Receta
    
    def setiD_Producto(self,iD_Producto):
        self.iD_Producto = iD_Producto
    def setnombre_Producto(self,nombre_Producto):
        self.nombre_Producto = nombre_Producto
    def setstock(self,stock):
        self.stock = stock
    def setprecio(self,precio):
        self.precio = precio
    def setgetunidad_de_medida(self,getunidad_de_medida):
        self.getunidad_de_medida = getunidad_de_medida
    def setiD_Receta(self,iD_Receta):
        self.iD_Receta = iD_Receta