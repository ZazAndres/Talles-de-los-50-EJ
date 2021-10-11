print("---Hallar el area y el perimetro de un circulo---")
r = float(input("Regaleme el radio del circulo: "))

import math
areaT=math.pi * r**2
perimetroT=2*math.pi*r

print(f"El area del circulo es: {areaT:2f}")
print(f"El perimetro del circulo es: {perimetroT:2f}")