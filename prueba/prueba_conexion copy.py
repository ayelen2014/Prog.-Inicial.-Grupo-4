import mysql.connector


class Conectar:
    def __init__(self, host, user, password,port, database):
        self.host = 'localhost'
        self.user = 'root'
        self.port = 3306
        self.password = '9111'
        self.database = 'bdnormativas'
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            port=self.port,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            print("Conexión exitosa a la base de datos.")
        else:
            print("Error al conectar a la base de datos.")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Desconexión exitosa de la base de datos.")
            
connection = Conectar(
    host='localhost',
    user='root', 
    password='9111',
    port='3306',
    database='bdnormativas'
)
# Establecer la conexión
connection.connect()
