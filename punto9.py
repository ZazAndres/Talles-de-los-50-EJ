print("---Hallar el promedio de numeros---")

cantNum=int(input("A cuantos numeros le va a sacar el promedio?:\n"))
listNum = []
for i in range(cantNum):
    listNum.append(float(input("Ingrese un numero: ")))

promedio = sum(listNum)/len(listNum)
print(f"El promedio de los numeros: {listNum} es {promedio}")
    