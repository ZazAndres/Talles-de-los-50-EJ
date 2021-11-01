print("---Dar la escritura inversa del numero dado de 4 cifras---")
x=int(input("Regalame un numero de 4 cifras: "))
c4= (x%10)*1000
c3= ((x%100)//10)*100
c2= ((x%1000)//100)*10
c1= (x%10000)//1000

print(f"{x} --> {c4+c3+c2+c1}")