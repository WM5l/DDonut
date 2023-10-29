# Crear un programa que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos.
# Es muy común usar variables para acumular valores.
print("Escriba un valor:")
n1 = int(input("$: "))
n2 = int(input("Escriba otro valor:\n$: "))
n3 = int(input("Escriba otro valor:\n$: "))
n4 = int(input("Escriba otro valor:\n$: "))
n5 = int(input("Escriba otro valor:\n$: "))

suma = n1 + n2 + n3 + n4 + n5

print("El promedio de los 5 valores es: \n$:", suma // 5)
