"""Properties"""


class Article:
    """Re-Escribir el ejercicio anterior utilizando una property en vez de un
    método de instancia.

    Restricciones:
        - Utilizar 3 variables de instancia
        - Utilizar 1 property
        - Utilizar 1 variable de clase
        - Utilizar 1 método de clase
        - No utilizar métodos de instancia
        - No utilizar Dataclasses
        - Utilizar Type Hints en todos los métodos y variables
    """
    __IVA: float = 0.21

    def __init__(self, nombre: str, costo: float, descuento: float = 0) -> None:
        self.nombre: str = nombre
        self.costo: float = costo 
        self.descuento: float = descuento

    @property
    def precio(self) -> float:
        precio: float = round (self.costo + (self.costo * self.__IVA),2)
        precio_final: float = round (precio - (self.descuento * precio),2)
        return precio_final

    def calcular_precio (self) -> float:
        precio_iva: float = round((self.costo * self.__IVA) + self.costo,2)
        precio: float = round((precio_iva - precio_iva * self.descuento),2)
        return precio

    @classmethod
    def actualizar_iva(cls, iva_nuevo: float) -> float:
        cls.__IVA: float = iva_nuevo
        return cls.__IVA


# NO MODIFICAR - INICIO
# Test parámetro obligatorio
try:
    article = Article()
    assert False, "No se puede instanciar sin nombre ni costo"
except TypeError:
    assert True

try:
    article = Article("Auto")
    assert False, "No se puede instanciar sin costo"
except TypeError:
    assert True

try:
    article = Article(nombre="Auto", costo=1)
    assert True
except TypeError:
    assert False, "El descuento es opcional"

try:
    article = Article(nombre="Auto", costo=1)
    article.precio = 2
    assert False, "No se puede modificar el precio"
except AttributeError:
    assert True


# Test básico
article = Article("Auto", 1)
assert article.nombre == "Auto"
assert article.precio == 1.21


article = Article("Auto", 1, 0.21)
assert article.nombre == "Auto"
assert article.precio == 0.96


# Test palabra clave
article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.precio == 1.21

article = Article(costo=1, nombre="Auto", descuento=0.21)
assert article.nombre == "Auto"
assert article.precio == 0.96


# Test de método de clase
Article.actualizar_iva(0.25)

article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.precio == 1.25
# NO MODIFICAR - FIN
