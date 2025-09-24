nomi = ["marco","luca","pietro"]
eta = [10, 11, 12]

while True:
    menu = int(input("inserisci un numero da 1 a 5: "))  # Spostata qui dentro
    
    if menu == 1:
        n = int(input("quante persone vuoi inserire: "))
        for i in range(n):
            nome = input("inserisci un nome: ")
            et = input("inserisci l'eta: ")
            nomi.append(nome)
            eta.append(et)
    if menu == 2:
        cerca_persona = input("quale nome vuoi cercare: ")
        print(cerca_persona)
        trovato = False
        for i in range(len(eta)):
            if cerca_persona == nomi[i]:
                print(eta[i])
                trovato = True
                break
        if not trovato:
            print("non è presente nella lista")
    if menu == 3:
        for i in range(len(nomi)):
            print(f"{i+1}. {nomi[i]}")
    if menu == 4:
        print(sum([int(e) for e in eta])/len(eta))
    if menu == 5:
        break
