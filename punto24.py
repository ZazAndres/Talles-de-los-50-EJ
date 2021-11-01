#reutilice el codigo del punto 6
cproducto=int(input("cantidad de productos escogidos: "))
listaproductos = []
for i in range(cproducto): #for in range me sirve para crear un bucle de con la cantidad ya dada 
    listaproductos.append(float(input("Digite el precio de los productos: "))) #.append me sirve para agregar elementos a la lista

Precioproductos = sum(listaproductos) #sumo los elementos de la lista con el SUM
precioiva = (Precioproductos * 19)/100
preciototal=Precioproductos+precioiva

 
print(f"El precio total a pagar con el IVA del 19% es... ${preciototal:.2f}")
print(f"El precio total a pagar sin el IVA del 19% es... ${Precioproductos:.2f}")
print(f"El valor del IVA 19% es... ${precioiva:.2f}")

#parte nueva
if preciototal >= 150000:
    print("Se aplica un descuento del 5%")
    x=((preciototal)*5)/100
    df5=preciototal-x
    print(f"El descuento final es de: {df5}")
else:
    print("No aplica el descuento del 5%")