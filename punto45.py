#50.	Construye un algoritmo y el respectivo diagrama de flujo que le solicite al usuario un número entero positivo, si el usuario digita un valor no permito, le debe volver a pedir el número. Una vez ingrese un valor válido deberá imprimir dicho valor.
n = int(input("Regaleme un numero: "))

while n < 0:
    print("Es un mal numero :c.")
    n = int(input("Regaleme un numero: "))

print("Es un buen numero :D.")  