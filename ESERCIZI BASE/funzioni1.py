# MODULARITA': suddividere il codice in funzioni.

#COSTANTE è una variabile globale
# ATTENZIONE!: COSTANTE è accessibile da tutte le funzioni soltanto in lettura!
COSTANTE = 3.14

def prima_lettera_maiuscola(stringa):
    """
    DOCSTRING: documentare una funzione:
    La funzione restituisce stringa 
    con la lettera iniziale maiuscola
    """
    #stringa è una variabile locale
    s = stringa[0].upper() + stringa[1:].lower()
    return s


def media(lista):
    """
    La funzione restituisce la media dei valori 
    presenti in lista e il numero di elementi di lista.
    """
    somma = 0.
    for val in lista:
        somma = somma + val
    n_lista = len(lista)
    media = somma / n_lista
    
    return media, n_lista # Si possono restituire più variabili

def main():
    nome = input("Inserisci un nome-> ")
    # print(help(prima_lettera_maiuscola))
    print(prima_lettera_maiuscola(nome))

    voti =[4.5, 6.25, 10, 8, 5.5, 9, 2, 3, 7, 7.7, 6.5]
    m, n = media(voti)
    print(f"Media: {m} | Numero di voti: {n}")

    if m >= 6.:
        print("GG") 
    

if __name__ == "__main__":
    main()