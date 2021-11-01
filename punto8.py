print("---Calcular el area de un hexagono---")

def area(n1, n2):
    area=(n1*n2)/2
    return area

def areairregular(l1,l2,l3,l4,l5,l6,h1,h2,h3,h4,h5,h6):
    areairregular= (l1*h1)/2 + (l2*h2)/2 + (l3*h3)/2 + (l4*h4)/2 + (l5*h5)/2 + (l6*h6)/2
    return areairregular

opcion = input("De que tipo es tu hexagono?:\n1.Regular\n2.Irregular\n")

if opcion == "1":
    n1=float(input("Ingrese el perimetro para hallar el area del hexagono: "))
    n2=float(input("Ingrese el apotema para hallar el area del hexagono: "))
    print("El area de tu hexagono regular es de: ",  area(n1, n2))

elif opcion=="2":
    l1=float(input("Ingrese el lado de tu primer triangulo: "))
    l2=float(input("Ingrese el lado de tu segundo triangulo: "))
    l3=float(input("Ingrese el lado de tu tercer triangulo: "))
    l4=float(input("Ingrese el lado de tu cuarto triangulo: "))
    l5=float(input("Ingrese el lado de tu quinto triangulo: "))
    l6=float(input("Ingrese el lado de tu sexto triangulo: "))
    h1=float(input("Ingrese la altura de tu primer triangulo: "))
    h2=float(input("Ingrese la altura de tu segundo triangulo: "))
    h3=float(input("Ingrese la altura de tu tercer triangulo: "))
    h4=float(input("Ingrese la altura de tu cuarto triangulo: "))
    h5=float(input("Ingrese la altura de tu quinto triangulo: "))
    h6=float(input("Ingrese la altura de tu sexto triangulo: "))
    print("El area de tu hexagono irregular es de: ", areairregular(l1,l2,l3,l4,l5,l6,h1,h2,h3,h4,h5,h6))