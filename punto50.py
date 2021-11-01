#dado un número determine la cantidad de números entre los cuales se puede dividir es decir sus factores.

def contardivisores(n):
    contadordivisores = 0

    for i in range(1, n+1):
        if n % i == 0:
            contadordivisores +=1
    return contadordivisores

n=int(input("Regaleme un numero: "))
print(f"Los divisores del numero {n} son: {contardivisores(n)}")