#Berrini Alejandro

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


print("Calcular el area de un rectángulo de base y altura ingresada por el usuario.")
base = int(input('Ingrese la medida de la base del rectangulo1: '))
altura = int(input('Ingrese la medida de la altura del rectangulo1: '))
base2 = int(input('Ingrese la medida de la base del rectangulo2: '))
altura2 = int(input('Ingrese la medida de la altura del rectangulo2: '))
base3 = int(input('Ingrese la medida de la base del rectangulo3: '))
altura3 = int(input('Ingrese la medida de la altura del rectangulo3: '))
rectangulo1 = Rectangulo(base, altura)
rectangulo2 = Rectangulo(base2, altura2)
rectangulo3 = Rectangulo(base3, altura3)
# mostramos
print(f'El area del rectangulo 1 es: {rectangulo1.calcular_area()}')
print(f'El area del rectangulo 2 es: {rectangulo2.calcular_area()}')
print(f'El area del rectangulo 3 es: {rectangulo3.calcular_area()}')
