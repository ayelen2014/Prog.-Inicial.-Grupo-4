from Modelo import *
from datetime import datetime


bd= panaderia()

def mostrarMenuPrincipal():
    print("\n+-------------------------------------------+")
    print("|                  PANADERIA                 |")
    print("+-------------------------------------------+\n")
    print("")
    print("MENÚ PRINCIPAL\n")
    print("[1] - INSERTAR UN PRODUCTO")
    print("[2] - ELIMINAR UN PRODUCTO")
    print("[3] - ACTUALIZAR UN PRODUCTO")
    print("[4] - SALIR")
    print("\n")

def insertarProducto():
    print("--------Insertar nuevo Producto--------")
    bd.ListarProducto()
    ID_Producto = int(input(f"Ingrese el tipo de Producto: "))
    Nombre = int(input("Ingrese el nombre del Producto: "))
    descripcion =  datetime.strptime(input("Ingrese una descripcion o fecha: DD/MM/AAAA : "), '%d/%m/%Y').date()
    precio = input("Ingrese nuevo precio : ")
    bd.ListarProducto()
    bd.insertarProducto(ID_Producto, Nombre, descripcion, precio)


def eliminarProducto():
    print("--------Eliminar--------")
    bd.consultarProducto()
    ID_Producto = int(input("Ingrese el producto a eliminar: "))
    bd.eliminarProducto(ID_Producto)

def actualizar():
    print("\n--------Actualizar Categoría--------\n")
    ID_Producto = int(input("Actualice nuevo Producto: "))
    Nombre = 'nombre del producto'
    Descripcion = input("Ingrese nueva descripcion: ")
    Precio = input ("Ingrese el nuevo precio: ")
    bd.actualizar_Producto(ID_Producto, Nombre, Descripcion, Precio)
    


def crearMenuPrincipal():
    opcion = " "
    while (opcion != 7):
        mostrarMenuPrincipal()
        opcion = int(input("Ingrese su opción: "))
        
        if opcion == 1:
            insertarProducto()
        elif opcion == 2:
           eliminarProducto()
        elif opcion == 3:
            actualizar()
        elif opcion == 4:
            print("Salir del menu")
            break
        else:
            print("Opción incorrecta")
      

def inicializar():
    crearMenuPrincipal()



inicializar()