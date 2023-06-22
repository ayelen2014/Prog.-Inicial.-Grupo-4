import Modelo

class Modelo:
       
    def ListarProducto():
        con = Modelo.Conectar()
        listado = con.ListarProducto()
        print("\n| ID PRODUCTO   |   NOMBRE PRODUCTO    |   STOCK   |   PRECIO   |  UNIDADA DE MEDIDA   |   ID RECETA   |")
        for producto in listado:
            print(' ',producto[0],"\t\t",producto[1],"\t\t",str(producto[2])+"\t\t $"+str(producto[3]),"\t\t",producto[4],"\t\t",producto[5])
            input("Para continuar presione enter")
            
    def InsertProducto():
        con = Modelo.Conectar()
        
        nombre_producto = input("\nIngrese el nombre del Producto ")
        stock = int(input("\nIngrese el stock del Producto: "))
        precio = int(input("\nIngrese el precio del Producto: "))
        unidad_de_medida= input("\nIngrese la unidad de medida del Producto: ")

        nuevoProducto= Modelo.Producto(0,nombre_producto,stock,precio,unidad_de_medida,0)

        con.InsertarProducto(nuevoProducto)
        input("Para continuar presione enter")