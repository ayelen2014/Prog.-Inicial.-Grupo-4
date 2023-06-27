import mysql.connector
from Conexion import *

class panaderia():
    def __init__(self):
        
        self.conexion = MySQLConnection("localhost","root","Wondershared98", "bd_grupo4", "3306")

    def ListarProducto(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM Productos")
        tipoProducto = cursor.fetchall()
        y=0
        x=0
        for i in tipoProducto:
            print(tipoProducto[y][0], tipoProducto[y][1])
            y+=1
        self.conexion.close()

    def insertarProducto(self, ID_Producto, Nombre, descripcion, precio):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        sql = "INSERT INTO producto(ID_Producto, Nombre, descripcion, precio) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql,(ID_Producto, Nombre, descripcion, precio))
        self.conexion.commit()
        cursor.close()
        self.conexion.close()

    def consultarProducto(self):
        self.conexion.connect()
        cursor=self.conexion.cursor()
        cursor.execute("SELECT * FROM producto")
        producto = cursor.fetchall()
        y=0
        x=0
        for i in producto:
            linea= ""
            for x in range (8):
                linea += str(producto[y][x]) + "  |  "
            y+=1
            print(linea)
        return
    
    def eliminarProducto(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM producto ")
        self.conexion.commit()
        print("Fue eliminado exitosamente")
        
    def actualizar_Producto(self, ID_Producto, Nombre, Descripcion, Precio):
        self.conexion.connect()
        query = "UPDATE categoria SET {} = %s WHERE ID_Producto = %s".format(ID_Producto)
        valores = (ID_Producto, Nombre, Descripcion, Precio)
        cursor = self.conexion.cursor()
        cursor.execute(query, valores)
        self.conexion.commit()
        if cursor.rowcount > 0:
            print("Campo actualizado exitosamente.")
        else:
            print("No se encontró el registro o no se realizaron cambios.")
            
    def Insumos(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM Insumos")
        Insumos = cursor.fetchall()
        y=0
        x=0
        for i in Insumos:
            print(Insumos[y][0], Insumos[y][1])
            y+=1
        self.conexion.close()

    def insertarInsumos(self, ID_Insumos, Nombre, Cantidad):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        sql = "INSERT INTO Insumos(ID_Insumos, Nombre, Cantidad) VALUES (%s,%s,%s)"
        cursor.execute(sql,(ID_Insumos, Nombre, Cantidad))
        self.conexion.commit()
        cursor.close()
        self.conexion.close()

    def consultarInsumos(self):
        self.conexion.connect()
        cursor=self.conexion.cursor()
        cursor.execute("SELECT * FROM Insumos")
        Insumos = cursor.fetchall()
        y=0
        x=0
        for i in Insumos:
            linea= ""
            for x in range (8):
                linea += str(Insumos[y][x]) + "  |  "
            y+=1
            print(linea)
        return
    
    def eliminarInsumos(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM Insumos ")
        self.conexion.commit()
        print("Fue eliminado exitosamente")    
        
        
    def actualizar_Insumos(self, ID_Insumos, Nombre, Cantidad):
        self.conexion.connect()
        query = "UPDATE categoria SET {} = %s WHERE ID_Insumos = %s".format(ID_Insumos)
        valores = (ID_Insumos, Nombre, Cantidad)
        cursor = self.conexion.cursor()
        cursor.execute(query, valores)
        self.conexion.commit()
        if cursor.rowcount > 0:
            print("Campo actualizado exitosamente.")
        else:
            print("No se encontró el registro o no se realizaron cambios.")
            
    def ProduccionDiaria(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM Produccion Diaria")
        ProduccionDiaria = cursor.fetchall()
        y=0
        x=0
        for i in ProduccionDiaria:
            print(ProduccionDiaria[y][0], ProduccionDiaria[y][1])
            y+=1
        self.conexion.close()

    def insertarProduccion(self, ID_Produccion, Fecha, CantidadProductos):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        sql = "INSERT INTO Produccion(ID_Produccion, Fecha, CantidadProductos) VALUES (%s,%s,%s)"
        cursor.execute(sql,(ID_Produccion, Fecha, CantidadProductos))
        self.conexion.commit()
        cursor.close()
        self.conexion.close()

    def consultarProduccion(self):
        self.conexion.connect()
        cursor=self.conexion.cursor()
        cursor.execute("SELECT * FROM Produccion")
        Produccion = cursor.fetchall()
        y=0
        x=0
        for i in Produccion:
            linea= ""
            for x in range (8):
                linea += str(Produccion[y][x]) + "  |  "
            y+=1
            print(linea)
        return
    
    def eliminarProduccion(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM Produccion ")
        self.conexion.commit()
        print("Fue eliminado exitosamente")
              
        
    def actualizar_Produccion(self, ID_Produccion, Fecha, Cantidad_Productos):
        self.conexion.connect()
        query = "UPDATE categoria SET {} = %s WHERE ID_Insumos = %s".format(ID_Produccion)
        valores = (ID_Produccion, Fecha, Cantidad_Productos)
        cursor = self.conexion.cursor()
        cursor.execute(query, valores)
        self.conexion.commit()
        if cursor.rowcount > 0:
            print("Actualizado exitosamente.")
        else:
            print("No se encontró el registro o no se realizaron cambios.")
            
    def ListarReceta(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM Receta")
        Receta = cursor.fetchall()
        y=0
        x=0
        for i in Receta:
            print(Receta[y][0], Receta[y][1])
            y+=1
        self.conexion.close()

    def insertarReceta(self, ID_Receta, ID_Producto, ID_Insumo, Cantidad_Usada):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        sql = "INSERT INTO Receta(ID_Receta, ID_Producto, ID_Insumo, Cantidad_Usada) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql,(ID_Receta, ID_Producto, ID_Insumo, Cantidad_Usada))
        self.conexion.commit()
        cursor.close()
        self.conexion.close()

    def consultarReceta(self):
        self.conexion.connect()
        cursor=self.conexion.cursor()
        cursor.execute("SELECT * FROM Receta")
        Receta = cursor.fetchall()
        y=0
        x=0
        for i in Receta:
            linea= ""
            for x in range (8):
                linea += str(Receta[y][x]) + "  |  "
            y+=1
            print(linea)
        return
    
    def eliminarReceta(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM Receta ")
        self.conexion.commit()
        print("Fue eliminado exitosamente")
        

    def actualizar_Receta(self, ID_Receta, ID_Producto, ID_Insumo, Cantidad_Usada):
        self.conexion.connect()
        query = "UPDATE categoria SET {} = %s WHERE ID_Insumos = %s".format(ID_Receta)
        valores = (ID_Receta, ID_Producto, ID_Insumo, Cantidad_Usada)
        cursor = self.conexion.cursor()
        cursor.execute(query, valores)
        self.conexion.commit()
        if cursor.rowcount > 0:
            print("Campo actualizado exitosamente.")
        else:
            print("No se encontró el registro o no se realizaron cambios.")
            
    def Empleados(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM Empleados")
        Empleados = cursor.fetchall()
        y=0
        x=0
        for i in Empleados:
            print(Empleados[y][0], Empleados[y][1])
            y+=1
        self.conexion.close()

    def insertarEmpleado(self, ID_Empleados, Nombre, Apellido, Puesto):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        sql = "INSERT INTO Empleado(ID_Empleados, Nombre, Apellido, Puesto) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql,(ID_Empleados, Nombre, Apellido, Puesto))
        self.conexion.commit()
        cursor.close()
        self.conexion.close()

    def consultarEmpleado(self):
        self.conexion.connect()
        cursor=self.conexion.cursor()
        cursor.execute("SELECT * FROM Empleado")
        Empleado = cursor.fetchall()
        y=0
        x=0
        for i in Empleado:
            linea= ""
            for x in range (8):
                linea += str(Empleado[y][x]) + "  |  "
            y+=1
            print(linea)
        return
    
    def eliminarEmpleado(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM Empleado ")
        self.conexion.commit()
        print("Fue eliminado exitosamente")

    def actualizar_Empleado(self, ID_Empleados, Nombre, Apellido, Puesto):
        self.conexion.connect()
        query = "UPDATE categoria SET {} = %s WHERE ID_Insumos = %s".format(ID_Empleados)
        valores = (ID_Empleados, Nombre, Apellido, Puesto)
        cursor = self.conexion.cursor()
        cursor.execute(query, valores)
        self.conexion.commit()
        if cursor.rowcount > 0:
            print("Campo actualizado exitosamente.")
        else:
            print("No se encontró el registro o no se realizaron cambios.")