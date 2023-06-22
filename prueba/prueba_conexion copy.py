import mysql.connector
from mysql.connector import Error 
class CONEXION():
        try:
                # Conexión a la base de datos
                conn = mysql.connector.connect(
                                        host='localhost',
                                        port=3308,
                                        user='root',
                                        password='',
                                        db='bd_novo_mundo'
                                        )
                if conn.is_connected():
                        print('conexion exitosa')
                        infoServer = conn.get_server_info()
                        print('La informacion del servidor es:',infoServer)
                        
 
        except Error as ex:
                print('Error durante la conexion',ex)

        finally:
                if conn.is_connected():
                        conn.close()
                print('La conexion ha finalizado')

