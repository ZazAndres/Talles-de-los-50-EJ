print("---Hallar la velocidad final---")
print("Regaleme las medidas en el sistema M.K.S")

def velocidadF(velocidadI,aceleracion,tiempo):
    vf=velocidadI+aceleracion*tiempo
    return vf

velocidadI = float(input("Regaleme la velocidad inicial: "))
aceleracion = float(input("Regaleme la acelaracion: "))
tiempo = float (input("Regalame el tiempo: "))

print(f"Los datos son:\nVelocidad Inicial: {velocidadI} m/s\nAceleración: {aceleracion} m/s^2\nTiempo: {tiempo} s")
print("La velocidad final es: ", velocidadF(velocidadI,aceleracion,tiempo), "m/s")