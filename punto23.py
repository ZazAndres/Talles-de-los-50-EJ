print("---determinar si un numero es par-positivo, \npar-negativo, impar-positivo o impar-negativo---")
num=int(input("Ingrese un numero: "))

if num%2 == 0:
    if num > 0:
        print(f"El numero {num}, es par-positivo.")
    else:
        print(f"El numero {num}, es par-negativo.")
else:
    if num > 0:
        print(f"El numero {num}, es impar-positivo.")
    else:
        print(f"El numero {num}, es impar-negativo.")