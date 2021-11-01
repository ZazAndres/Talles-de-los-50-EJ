print("---Determinar la suma de numeros naturales---")
x = int(input("¿Desde que numero?: "))

def generarNaturales(n):
    Naturales = []
    contador = x

    while contador <= n:
            Naturales.append(contador)
            contador += 1
        
    return Naturales

n = int(input("¿Hasta que numero?: "))

if n > 0:
    Naturales = generarNaturales(n)

    print(Naturales)
    print("Cantidad de naturales: ", len(Naturales))
    print("La suma de los naturales es: ", sum(Naturales))

else:
    print("El numero debe ser positivo.")