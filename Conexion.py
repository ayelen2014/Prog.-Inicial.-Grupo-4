import mysql.connector
from Producto import Producto

class Conectar:
    def __init__(self, host, user, password, database, port):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'password'
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


db = Conectar('localhost', 'root', 'password', 'bd_grupo4', 'port')

while True:
    print("Seleccione una opción:")
    print("1. Conectar a la base de datos")
    print("2. Desconectar de la base de datos")
    print("3. Insertar datos")
    print("4. Seleccionar datos")
    print("5. Salir")

    option = input("Opción seleccionada: ")

    if option == "1":
        db.connect()
    elif option == "2":
        db.disconnect()
    elif option == "3":
        table = input("Ingrese el nombre de la tabla: ")
        data = input("Ingrese los datos a insertar: ")
        db.insert_data(table, data)
    elif option == "4":
        table = input("Ingrese el nombre de la tabla: ")
        result = db.select_data(table)
        for row in result:
            print(row)
    elif option == "5":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

