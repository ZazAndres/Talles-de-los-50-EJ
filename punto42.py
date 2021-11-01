print("---Imprimir los numeros naturales---")

def generarNaturales(n):
    Naturales = []
    contador = 0

    while contador <= n:
            Naturales.append(contador)
            contador += 1

    return Naturales

n = int(input("Escriba la cantidad de numeros naturales que quiere generar: "))

if n > 0:
    Naturales = generarNaturales(n)

    print(Naturales)
    print("Cantidad de naturales: ", len(Naturales))

else:
    print("El numero debe ser positivo.")