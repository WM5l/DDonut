# Crear una función que reciba un entero y que retorne (devuelva) el resto y el cociente.


def mar(ent1, ent2):
    div = ent1 // ent2
    rest = ent1 % ent2
    return rest, div


ent1 = int(input("Ingrese un entero:\n$: "))
ent2 = int(input("Ingrese otro entero\n$: "))

resul_rest, result_coci = mar(ent1, ent2)

print(f"El resto de los enteros en: {resul_rest}")
print(f"El cociente de los enteros es: {result_coci}")
