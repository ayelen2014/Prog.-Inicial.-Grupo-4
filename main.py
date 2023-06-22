import Controlador
from Producto import Producto

while True:
    print("\n+-------------------------------------------+")
    print("|                  PANADERIA                |")
    print("|                Big Bread SA               |")
    print("+-------------------------------------------+\n")
    print("")
    print("MENÚ PRINCIPAL\n")
    print("1 - INGRESAR / ELIMINAR / MODIFICACION DE PRODUCTO")
    print("2 - ALTA / BAJA / MODIFICAR INSUMOS")
    print("3 - ALTA / BAJA / MODIFICAR PRODUCCIÓN DIARIA")
    print("4 - ALTA / BAJA / MODIFICAR RECETAS")
    print("5 - LISTA DE PRODUCTOS")
    print("6 - LISTA DE PRODUCCIÓN EN UN INTERVALO")
    print("7 - LISTA DE INSUMOS DIARIO")
    print("8 - SALIR")
    print("\n")
    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        Controlador.InsertarProducto()
    elif opcion == 2:
        None
    elif opcion == 3:
        None
    elif opcion == 4:
        None
    elif opcion == 5:
        Controlador.ListarProducto()
    elif opcion == 6:
        None
    elif opcion == 7:
        None
    elif opcion == 8:
        break
    else:
        print("¡Opción incorrecta!")