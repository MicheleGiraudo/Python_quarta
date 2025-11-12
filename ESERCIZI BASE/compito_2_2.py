# Scrivi un programma che permetta all' utente di effettuare le quattro
# operazioni aritmetiche. Per prima cosa chiede all'utente quale operazione desidera eseguire
# 0: somma | 1: sottrazione | 2: moltiplicazione | 3: divisione
# poi chiede all' utente due numeri e stampa il risultato dell' operazione.

print("Inserire 0 per effettuare una SOMMA.") 
print("Inserire 1 per effettuare una SOTTRAZIONE.")
print("Inserire 2 per effettuare una MOLTIPLICAZIONE.")
print("iInserire 3 per effettuare una DIVISIONE.")

operazione = int(input("Inserisci per l' operazione-> "))
a = int(input("Inserisci un numero-> "))
b = int(input("Inserisci un altro numero-> "))

if operazione == 0:
    ris = a + b
    print(f"Il risultato e' {ris}")
elif operazione == 1:
    ris = a - b 
    print(f"Il risultato e' {ris}")
elif operazione == 2:
    ris = a*b
    print(f"Il risultato e' {ris}")
elif operazione == 3:
    ris = a/b
    print(f"Il risultato e' {ris}")
else:
    print("Numero di menu' inserito non valido")

