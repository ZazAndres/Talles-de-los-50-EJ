print("---Determinar la energia---")
print("Regaleme las medidas en el sistema M.K.S")
def energia(a,b):
    ener=1/2*a*b**2
    return ener

masa = float(input("Ingresar la masa del objeto: "))
velocidad = float(input("Ingresar la velocidad del objeto: "))

print(f"Los datos son:\nMasa: {masa} kg\nVelocidad: {velocidad} m/s")
print("La energia (en Jouls) del objeto es: ", energia(masa,velocidad),"J")