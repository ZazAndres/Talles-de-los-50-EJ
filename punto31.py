print("--Determinar el valor de pasaje de un avion--")
dis=int(input("¿Cual es la distancia(En km) del viaje?: "))
ndias= int(input("¿Cuantos dias estaras de estancia?: "))

presdis = dis * 5000

if dis>1000 and ndias>7: 
    print("Se le hace un descuento del 15%")
    print(f"El valor del pasaje es del ${presdis*0.15}")
elif presdis<100000:
    print(f"El minimo a cobrar es de $100000, y su valor da {presdis}")
else:
    print(f"El valor del pasaje es del ${presdis}")
