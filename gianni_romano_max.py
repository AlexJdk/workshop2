def trova_massimo():
    lista_numeri = [float(x) for x in input("Inserisci una lista di numeri separati da spazi:   ").split()]
    risultato = max(lista_numeri)
    print(risultato)

def scelta_utente():
    scelta = input('Desideri continuare? y/n ')

    if scelta == 'y' or scelta == 'Y':
        trova_massimo()
        scelta_utente()
    elif scelta == 'n' or scelta == 'N':
        print('Ti auguro una buona giornata!')
    else:
        print('Per favore, scrivi un inpur richiesto')
        scelta_utente()

print('Benvenuto!')
trova_massimo()
scelta_utente()