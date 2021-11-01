print("---Calcular la nota final---")

n1=float(input("Regaleme la primera nota: "))
n2=float(input("Regaleme la segunda nota: "))
n3=float(input("Regaleme la tercera nota: "))
n4=float(input("Regaleme la cuarta nota: "))
n5=float(input("Regaleme la quinta nota: "))

nfinal=((n1*15)/100)+((n2*20)/100)+((n3*15)/100)+((n4*30)/100)+((n5*20)/100)
    
if nfinal < 2:
    print(f"-Tu nota es {nfinal}, por lo tanto no puedes habilitar-")
elif nfinal < 3:
    print(f"-Tu nota es {nfinal}, por lo tanto reprobaste-")
elif nfinal >= 3 and nfinal < 4.5:
    print(f"-Tu nota es {nfinal}, por lo tanto aprobaste-")
else:
    print(f"-Tu nota es {nfinal}, felicitación al estudiante, aprobaste la materia-")