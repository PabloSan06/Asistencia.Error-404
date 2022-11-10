class cubo:
    def __init__ (self, altura, ancho, profundidad):
        self.altura = altura
        self.ancho = ancho
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.altura * self.ancho * self.profundidad

altura = int(input('Ingrese la altura del cubo: '))
ancho = int(input('Ingrese el ancho del cubo: '))
profundidad = int(input('Ingrese la profundidad del cubo: '))

cubo1 = cubo(altura, ancho, profundidad)
print(f'El volumen del cubo es: {cubo1.calcular_volumen()}')