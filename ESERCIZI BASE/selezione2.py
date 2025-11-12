# Creazione di un menù
print("Premi A per inserire.")
print("Premi B per modificare.")
print("Premi C per cancellare.")

tasto = input("-> ")
tasto = tasto.upper()  # Trasforma qualsiasi tasto in maiuscolo (se è già maiuscolo rimane tale)
# tasto = tasto.lower() ---> trasforma qualsiasi tasto in minuscolo

if tasto == "A":
    print("L'utente vuole inserire.")
elif tasto == "B":                      # "elif" serve per aggiungere condizione
    print("L'utente vuole modificare.")
elif tasto == "C":
    print("L'utente vuole cancellare.")
else:
    print("Tasto non valido.")