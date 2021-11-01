print("---Imprimir los numeros pares positivos---")

def generarPares(n):
    pares = []
    contador = 0
    numero = 0

    while contador < n:
        if numero % 2 == 0: 
            pares.append(numero)
            contador += 1
        
        numero += 1
    return pares

n = int(input("Escriba la cantidad de pares positivos que quiere generar: "))

if n > 0:
    pares = generarPares(n)

    print(pares)
    print("Cantidad de pares: ", len(pares))

else:
    print("El numero debe ser positivo.")