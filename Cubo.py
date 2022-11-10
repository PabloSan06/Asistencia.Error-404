class Cubo:
    """
    creamos la clase Cubo con los atributos, ancho, alto, profundidad, con
    un metodo calcular_volumen que tendra la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores
    """
    def __init__(self, altura, ancho, profundidad):
        self.altura = altura
        self.ancho = ancho
        self.profundidad = profundidad
    
    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad

ancho = int(input("Digite el ancho del cubo: "))
altura = int(input("Digite el altura del cubo: "))
profundidad = int(input("Digite la profundidad del cubo: "))    

cubo1 = Cubo(ancho, altura, profundidad)
print(f"El volumen del cubo es: {cubo1.calcular_volumen()}")

"""Alsina maximiliano"""