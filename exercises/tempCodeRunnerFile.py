    __iva=0.21

    def __init__(self, nombre, costo, descuento=0):
        self.nombre = nombre
        self.costo = costo
        self.descuento = descuento
    
    @property
    def precio(self):
        precio = round(self.costo + (self.costo * self.__iva),2)
        precio_final = round(precio - (self.descuento * precio),2)
        return precio_final

    @classmethod
    def actualizar_iva(cls,iva):
        cls.__iva=iva