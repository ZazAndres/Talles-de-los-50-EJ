nombre = input("Por favor digitime su nombre: ")
cualificativo = input("Escriba su apodo: ")
edad = int(input("Escriba su edad: "))

if edad <= 25:
    print(nombre,cualificativo,", eres un bebesito")
else:
    print(f"{nombre}{cualificativo}, eres un viejo")