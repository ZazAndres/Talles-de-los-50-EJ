num = float(input("Por favor regaleme un numero decimal: "))

entera = num//1
num %= 1
print(f"la parte entera es {entera}")
print(f"la parte decimla es {num:.3f}")