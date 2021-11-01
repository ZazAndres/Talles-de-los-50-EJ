import math
print("---Calcular la diastancia entre dos puntos en el plano cartesiano---")
punto1 = input("Ingrese la coordenada del primer punto (x1, y1) separando los dos valores por coma(,): ")
punto2 = input("Ingrese la coordenada del primer punto (x2, y2) separando los dos valores por coma(,): ")

punto1 = punto1.split(",")#Utilizando la funcion .split() para separar los datos por espacio y asignarlos a la variable punto1 y puento2
punto2 = punto2.split(",")

x1 = eval(punto1[0])#utilanzo la funcion eval() convierte el tipo de cadena a tipo de datos
y1 = eval(punto1[1])
x2 = eval(punto2[0])
y2 = eval(punto2[1])

distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f"La distancia entre el punto {x1},{y1} y {x2},{y2} es: {distancia}")