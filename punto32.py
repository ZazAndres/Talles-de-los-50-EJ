print("---Saber si un año es bisiesto---")
año = int(input("¿Que año es?: "))

if año%4==0 and año%100!=0:
    print(f"El año {año} es bisiesto.")
elif año%400==0:
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")