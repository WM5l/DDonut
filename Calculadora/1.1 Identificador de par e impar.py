# Crear un programa que le solicite al usuario un entero y determine si es par, mostrando por pantalla un
#   mensaje que indique el resultado.
#   Para determinar si un número es par o impar, se puede determinar con el uso del operador %, les
#   dejamos a ustedes el cómo.


x = int(input(f"Introduca: "))


def par():
    user = x
    if user % 2 == 0:
        print("Es par")
    else:
        print("No es par")


par()

print(par)
