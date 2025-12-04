print("inserisci il numero corrispondente alla figura per calcolare il suo perimetro/circonferenza")

print()

print("""
- Quadrato: >>> 1
- Cerchio: >>> 2
- Rettangolo: >>> 3
""")

print()

figura=input('inserisci un numero: >>>   ')

if figura == '1':
    Lato=float(input('Determina la lunghezza del lato: '))
    Perimetro = Lato * 4

    print()


    print("Il suo perimetro è:", "{:.2f}".format(Perimetro))

    print()

    print(" A presto! (;")

elif figura == '2':
    Raggio=float(input('Determina il raggio: '))
    Circonferenza = (2 * 3.14) * Raggio
    
    print()

    print("La sua circonferenza è:", "{:.2f}".format(Circonferenza))

    print()

    print(" A presto! (;")

elif figura == '3': 
    Base=float(input('Determina la base: '))
    Altezza=float(input('Determina l\'altezza: '))
    Perimetro = (Base * 2) + ( Altezza * 2)

    print()


    print("Il suo perimetro è:", "{:.2f}".format(Perimetro))

    print()

    print(" A presto! (;")
else:
     print("devi selezionare  un numero!")


