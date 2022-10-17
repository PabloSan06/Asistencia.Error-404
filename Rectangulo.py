class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tenér 2 atributos: altura y base
    el nombre del método sera calcular_arear utilizando la formula:
    area = base * altura. pero la base y la altura debe ser ingresado por teclado
    y los objetos deben ser tres
    """
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base


print("Ejercicio numero 10: Calcularel area de un rectangulo")
base = int(input('\nDigite el numero de la base: '))
altura = int(input('\nDigite la altura: '))
rectangulo1 = Rectangulo(base, altura)
# mostramos
print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')

"""BRIAN AHUMADA"""
