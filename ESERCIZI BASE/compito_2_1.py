# Scrivi un programma Python nel quale assegni alla variabile lista_voti
# una lista con tutti i tuoi voti (almeno 6 voti). Sfrutta l'indicizzazione per:
# - stampare la lista senza il primo e l'ultimo voto;
# - sostituire il quarto voto con un 10;
# - stampare i primi 3 voti della lista;

registro = [3, 8, 9, 6.5, 6.75, 10]

for voto in registro[:-1]:
    print(voto)

print(f"Sostituisco il quarto voto con un 10...")

for voto in registro[:3]:
    print(voto)