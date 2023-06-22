import pymysql

# Conexión a la base de datos
conn = pymysql.connect(
        host='localhost',
        port=3308,
        user='root',
        password='',
        db='bd_novo_mundo'
)

# Crear un objeto cursor
cursor = conn.cursor()

# Crear una tabla
tabla_sql = '''
CREATE TABLE Empleados2 (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Edad INT
)
'''

cursor.execute(tabla_sql)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
