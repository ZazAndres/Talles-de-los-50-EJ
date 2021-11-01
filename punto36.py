print("---Ordenar tres numeros---")

listanumeros = []
x=3
for i in range(x):
    listanumeros.append(int(input("Deme un numero: ")))

print(f"Los numeros de menor a mayor es {sorted(listanumeros)}")
print(f"Los numeros de mayor a menor es {sorted(listanumeros, reverse=True)}")