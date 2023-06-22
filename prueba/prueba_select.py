import mysql.connector
from mysql.connector import Error
def establecer_conexion():


        conn = mysql.connector.connect(
                host='localhost',
                port=3308,
                user='root',
                password='',
                db='bd_novo_mundo'
        )
        return conn

def obtener_empleados():
    conn = establecer_conexion()

    with conn.cursor() as cursor:
        # Consulta para obtener todos los empleados
        select_query = "SELECT * FROM Empleados"
        cursor.execute(select_query)
        empleados = cursor.fetchall()

        # Imprimir los resultados
        for empleado in empleados:
            print(empleado)

    # Cerrar la conexión
    conn.close()

# Ejecutar la función para obtener los empleados
obtener_empleados()