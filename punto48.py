#39.	Escribe un algoritmo o el respectivo diagrama de flujo que lea 3 números e indique si al menos 2 de ellos son iguales 

print("---Comparacion de numeros---")
n=int(input("Deme un numero: "))
x=int(input("Deme un numero: "))
y=int(input("Deme un numero: "))

if n != x:
    print(f"{n} es diferente a {x}")
else:
    print(f"{n} es igual a {x}")

if n != y:
    print(f"{n} es diferente a {y}")
else:
    print(f"{n} es igual a {y}")

if y != x:
    print(f"{y} es diferente a {x}")
else:
    print(f"{y} es igual a {x}")