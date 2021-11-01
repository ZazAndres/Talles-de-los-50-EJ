print("---Imprimir los numeros impares positivos---")

def generarImpares(n):
    impares = []
    contador = 0
    numero = 0

    while contador < n:
        if numero % 2 != 0: 
            impares.append(numero)
            contador += 1
        
        numero += 1
    return impares

n = int(input("Escriba la cantidad de impares positivos que quiere generar: "))

if n > 0:
    impares = generarImpares(n)

    print(impares)
    print("Cantidad de impares: ", len(impares))

else:
    print("El numero debe ser positivo.")