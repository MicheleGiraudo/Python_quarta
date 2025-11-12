# Crea un programma in Python che chiede all' utente il suo nome e lo stampa sempre con l'iniziale maiuscola
nome = input("Inserisci il tuo nome tutto minuscolo --> ")
nome = nome[0].upper() + nome[1:]  # Da 1 alla fine
print(nome)



# Crea un programma in Python che chiede all' utente un numero intero e stampa se
# il numero è divisibile per 2, per 3, o per 5. (Hint: usare operatore % per il resto della divisione)

numero = int(input("Inserisci un numero --> "))

if numero % 2 == 0:
    print("Il numero è divisibile per 2")
elif numero % 3 == 0:
    print("Il numero è divisibile per 3")
elif numero % 5 == 0:
    print("Il numero è divisibile per 5")



# Crea un programma in Python che chiede all'utente una frase e stampi
# la stringa a caratteri alternati

stringa = input("Inserisci una frase -->")
print(f"{stringa[::2]}")  # : -> dall' inizio, : -> alla fine, 2 -> gap (salto)


# Crea un programma in Python che chiede all'utente una frase e stampi
# la frase al contrario

stringa = input("Scrivi una frase --> ")
print(f"{stringa[::-1]}") # stessa cosa di prima ma salta di -1