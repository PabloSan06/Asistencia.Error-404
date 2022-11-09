"""
Definir una clase padre llamada vehiculo y dos clases hijas llamdas Auto y bicicleta,
las cuales heredan de la clase padre vehiculo. 

La clase padre debe tener los siguientes atributos y metodos:
Vehiculo(clase padre)
Atributos:color, ruedas
metodos: init(color,ruedas) y str

Auto(clase hija)
Atributos:velocidad(km/hs)
metodos: init(color,ruedas,velocidad) y str

Bicicleta(clase hija)
Atributos:tipo(urbana,montaña,etc)
metodos: init(color,ruedas,tipo) y str

"""
#Clase padre
class Vehiculo:
  def __init__(self, color, ruedas):
    self.color = color
    self.ruedas = ruedas

  def __str__(self):
    return f"Color: {self.color}, ruedas: {self.ruedas}"

#Clase hija
class Auto(Vehiculo):
  def __init__(self, color, ruedas, velocidad):
    super().__init__(color, ruedas)
    self.velocidad = velocidad

  def __str__(self):
    return f"{super().__str__()} velocidad(km/h): {self.velocidad}" 

#Clase hija
class Bicicleta(Vehiculo):
  def __init__(self, color, ruedas, tipo):
    super().__init__(color, ruedas)
    self.tipo = tipo

  def __str__(self):
    return f"{super().__str__()} tipo: {self.tipo}"

# Instanciamos un objeto de cada clase
# Instancio un objeto de la clase Vehiculo
moto = Vehiculo("Negro", 2)
print(moto)

# Instancio un objeto de la clase Auto
auto = Auto("Azul", 4, 90)
print(auto)

# Instancio un objeto de la clase Bicicleta
bicicleta = Bicicleta("Negra", 2, "Mountain Bike")
print(bicicleta)
