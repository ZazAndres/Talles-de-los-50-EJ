#51.	Construye un algoritmo y el respectivo diagrama de flujo que permita leer una cantidad variable de números y nos indique cuantos fueron mayores a 100 y cuántos menores a 100.
y="si"
listmen100 = []
listmay100 = []

while y == "si":
    x = int(input("Regaleme un numero: "))
    if x<100:
        listmen100.append(x)
    else:
        listmay100.append(x)
    y = input("Quieres seguir? ")

print(f"{len(listmay100)} fueron mayores a 100: {listmay100}")

print(f"{len(listmen100)} fueron menores a 100: {listmen100}")