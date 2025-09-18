n = int(input("Inserisci un numero: "))
fattoriale = 1

for i in range(1, n + 1):
    fattoriale *= i

print("Il fattoriale di", n, "è:", fattoriale)

    