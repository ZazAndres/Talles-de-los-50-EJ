print("---Comparacion de dos numeros---")
n1=float(input("Regaleme el primer numero: "))
n2=float(input("Regaleme el segundo numero: "))

if n1>n2:
    print(f"{n1} > {n2}\n-{n1} es mayor\n-{n2} es el menor")
elif n1<n2:
    print(f"{n1} < {n2}\n-{n2} es mayor\n-{n1} es el menor")