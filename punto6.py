cproducto=int(input("cantidad de productos escogidos: "))
listaproductos = []
for i in range(cproducto): #for in range me sirve para crear un bucle de con la cantidad ya dada 
    listaproductos.append(float(input("Digite el precio de los productos: "))) #.append me sirve para agregar elementos a la lista

PrecioTotal = sum(listaproductos) #sumo los elementos de la lista con el SUM
precioiva = (PrecioTotal * 19)/100

print(f"El precio total a pagar con el IVA del 19% es... ${PrecioTotal+precioiva:.2f}")
print(f"El precio total a pagar sin el IVA del 19% es... ${PrecioTotal:.2f}")
print(f"El valor del IVA 19% es... ${precioiva:.2f}")