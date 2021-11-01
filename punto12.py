print("---Hallar la distancia recorrida---")
print("Regaleme las medidas en el sistema M.K.S")

def Distancia(tiempo,aceleracion,velocidad):
    x= (velocidad * tiempo + aceleracion * tiempo)/ 2
    return x

tiempo=float(input("Regaleme el tiempo en segundos: "))
aceleracion = float(input("Regaleme la aceleracion: "))
velocidad = float(input("Regaleme la velocidad: "))

print(f"Los datos son:\nVelocidad: {velocidad} m/s\nAceleración: {aceleracion} m/s^2\nTiempo: {tiempo} s")
print("La distancia recorrida es:", Distancia(tiempo,aceleracion,velocidad),"Metros")