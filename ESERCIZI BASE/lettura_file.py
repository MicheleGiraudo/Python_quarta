file = open("./dati.csv", "r")  # oggetto file
righe = file.readlines() # Funzione che restituise una lista di stringhe contenenti le righe
file.close()

prima_riga = righe[0]

titoli = righe[0][:-1].split(",")
print(titoli)

#unpacking (=spacchettamento)
titolo1, titolo2, titolo3 = prima_riga[:-1].split(",")
print (titolo1)

# leggere tutte le altre righe del file e stamparle, usare un ciclo FOR pythonico
for riga in righe:
    print (riga)