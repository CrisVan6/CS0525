print("Genera il nome della tua band!")

print()

nome_città = input('Inserisci il nome della tua città di origine: ')

print()

risposta = input('Hai un\' animale domestico? (si/no) ')

print()

if risposta == 'si':

    nome_animale = input('Inserisci il nome del tuo animale domestico: ')
else:
    nome_animale = input('Allora quale nome daresti al tuo ipotetico animale domestico?: ')

print()

nome_band = nome_città + '  ' + nome_animale
print(f"Il nome della band sarà: {nome_band}")

