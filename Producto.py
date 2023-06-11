class Producto():
    ID_Producto =0,
    Nombre = "",
    Descripcion =0,
    Precio = 0,
    

    def __init__(self,iD_Producto,nombre,descripcion,precio):
        self.ID_Producto = iD_Producto
        self.Nombre =nombre
        self.Descripcion = descripcion
        self.Precio = precio

    
    def getiD_Producto(self):
        return self.iD_Producto
    def getnombre_Producto(self):
        return self.Nombre
    def getstock(self):
        return self.Descripcion
    def getprecio(self):
        return self.precio

    
    def setiD_Producto(self,iD_Producto):
        self.iD_Producto = iD_Producto
    def setnombre_Producto(self,nombre):
        self.nombre = nombre
    def setstock(self,descripcion):
        self.descripcion = descripcion
    def setprecio(self,precio):
        self.precio = precio