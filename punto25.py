#25.Escribe un algoritmo que lea un número y si este es mayor o igual a 10 devuelva el triple de este, de lo contrario la cuarta parte de este.
print("---Inicio del programa---")
num=int(input("Regaleme un numero: "))

if num >= 10:
    num *= 3
    print(f"El triple es: {num}")
else:
    num/=4
    print(f"La cuarta parte es: {num}")

print("Fin del programa.")