print("---Comparacion de numeros---")
n1=float(input("Inserte el primer numero: "))
n2=float(input("inserte el segundo numero: "))
n3=float(input("inserte el tercer numero: "))
c1= n1+n2

print(f"La sumatoria del numero 1 y el numero 2 es: {n1} + {n2} = {c1}")
if c1>n3:
    print(f"El numero mayor es {c1}")
    print(f"El numero menor es {n3}")
else:                                                   
    print(f"El numero mayor es {n3}")
    print(f"El numero menor es {c1}")