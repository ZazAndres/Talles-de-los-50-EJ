print("---Comparacion de tres numeros---")
n1=float(input("Regaleme el primer numero: "))
n2=float(input("Regaleme el segundo numero: "))
n3=float(input("Regaleme el tercer numero: "))

if n1>n2 and n1>n3:
    if n2 > n3:
        print(f"El numero mayor es {n1}")
        print(f"El numero menor es {n3}")
    else:
        print(f"El numero mayor es {n1}")
        print(f"El numero menor es {n2}")
elif n2>n1 and n2>n3:
    if n1 > n3:
        print(f"El numero mayor es {n2}")
        print(f"El numero menor es {n3}")
    else:
        print(f"El numero mayor es {n2}")
        print(f"El numero menor es {n1}")
elif n3>n1 and n3>n2:
    if n2 > n1:
        print(f"El numero mayor es {n3}")
        print(f"El numero menor es {n1}")
    else:
        print(f"El numero mayor es {n3}")
        print(f"El numero menor es {n2}")