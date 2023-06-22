import mysql.connector
from mysql.connector import Error

class conexion():

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
                        infoServer = conexion.get_server_info()
                        print('info del servidor:', infoServer)
                        cursor =  conexion.cursor()
                        cursor.execute("INSERT INTO empleados (nombre) VALUES ('Fernando')")
                        conexion.commit()
                        print("Registro insertado con éxito")
        
        except Error as ex:
                print('Error durante la conexion',ex)

        finally:
                if conexion.is_connected():
                        conexion.close()
                print('La conexion ha finalizado')
                        