print("---Imprimir el dia de la semana---")
n = int(input("Ingrese el numero del dia de la semana (entre el 1 y el 7): "))

if n <= 7:
    listas = ["x", "Lunes", "Martes", "Miercoles", "jueves", "Viernes", "Sabado", "Domingo"]
    print(f"El {n} le coresponde el dia: {listas[n]}")
else:
    print("Ingrese correctamente el numero del dia de la semana.\n1->Lunes, 2-> Martes...")    