print("Inicio del programa")
dinero= int(input("Ingrese la cantida de dinero COP: $"))
x=1

while x==1:
    print("billetes de:")
    print(f"$100k: {int(dinero/100000)}")
    dinero = dinero%100000

    print(f"$50k: {int(dinero/50000)}")
    dinero = dinero%50000

    print(f"$20k: {int(dinero/20000)}")
    dinero = dinero%20000

    print(f"$10k: {int(dinero/10000)}")
    dinero = dinero%10000

    print(f"$5k: {int(dinero/5000)}")
    dinero = dinero%5000

    print(f"$2k: {int(dinero/2000)}")
    dinero = dinero%2000

    print(f"$1k: {int(dinero/1000)}")
    dinero = dinero%1000

    print("monedas de:")

    print(f"$500: {int(dinero/500)}")
    dinero = dinero%500

    print(f"$200: {int(dinero/200)}")
    dinero = dinero%200

    print(f"$100: {int(dinero/100)}")
    dinero = dinero%100

    print(f"$50: {int(dinero/50)}")
    dinero = dinero%50

    break

print("fin del programa.")
