                                        # RODRIGO CHAVEZ #

# Ejercicio 10: No repetir caracteres.
# hacer un programa que pida una cadena por teclado, luego
# meter los caracteres en una lista sin repetir los caracteres

cadena = input("Dame una cadena: ")

print(cadena)

lista = []

for i in cadena:
    if (i not in lista): # Si el caracter aun no esta en la lista
        lista.append(i) # Lo agregamos a la lista

print(f"\nlista de caracteres sin repetir ninguno: \n {lista}")
                                        
                                        # RODRIGO CHAVEZ #
