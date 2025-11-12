# Programma che, richiesto n numeri in input, restituisce la somma dei primi n numeri dispari

import math  # Libreria

n = int(input("Inserisci un numero -->"))
somma = 0

if n >= 0: 
    for i in range(1, 2 * n + 1, 2):
        print(i)
        somma += i

radice_intera = math.isqrt(somma)
print(f"La somma è: {somma}, quadrato perfetto: {radice_intera ** 2 == somma}") # Condizione nella stringa (stampa TRUE o FALSE)
                                                                                # **2 eleva al quadrato