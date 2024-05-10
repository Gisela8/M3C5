#Ejercicio 1:
#Cree un bucle For de Python.
print("\033[1m" + "Ejercicio 1" + "\033[0m")
ejercicio = "Ejercicio 1"

frutas = ["Manzana", "Naranja", "Fresa",
          "Guayaba"] 

for fruta in frutas:
    if fruta == "Manzana":
        print(f"La {fruta} no es la fruta con más vitamina C")

    elif fruta == "Guayaba":
        print(f"La {fruta} es la fruta con más vitamina C")
        #break
    else:
        print(f"La {fruta} tiene mucha vitmania C")

#Ejercicio 2:
#Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
print()
print("\033[1m" + "Ejercicio 2" + "\033[0m")


def suma(a, b, c):
    return a + b + c


print(suma(2, 4, 6))

#Ejercicio 3:
#Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
print()
print("\033[1m" + "Ejercicio 3" + "\033[0m")

suma = lambda a, b, c: a + b + c
print(suma(2, 4, 6))

#Ejercicio 4:
# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista.
# Sugerencia, si es necesario, utilice un bucle for in y el operador in.
print()
print("\033[1m" + "Ejercicio 4" + "\033[0m")

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

for nombre_lista in lista_nombre:
    if nombre_lista == nombre:
        print(f"{nombre} aparece en la lista")
        break
else:
    print(f"{nombre} no aparece en la lista")
