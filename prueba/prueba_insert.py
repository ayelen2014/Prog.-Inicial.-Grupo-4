import mysql.connector
from mysql.connector import Error

try:
        conexion = mysql.connector.connect(
                host='localhost',
                port=3308,
                user='root',
                password='',
                db='bd_novo_mundo'
        )

        if conexion.is_connected():
            print('conexion exitosa')
            cursor =  conexion.cursor()
            cursor.execute("INSERT INTO empleados (nombre) VALUES ('JOSE')")
            conexion.commit()
            print("Registro insertado con éxito")
except Error as ex:
        print('Error durante la conexion',ex)

finally:
       if conexion.is_connected():
        conexion.close()
        print('La conexion ha finalizado')
                