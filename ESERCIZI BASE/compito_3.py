# Programma python che chiede all' utente un numero di bit e un numero binario,
# se la lunghezza del numero binario è minore del numero di bit aggiungere tot zeri
# per arrivare al numero di bit inserito

bit = int(input("Inserisci il massimo numero di bit che vuoi utilizzare-> "))
num_bin = input("Inserisci un numero binario-> ")

if len(num_bin) <= bit:
    num_bin = '0' *(bit - len(num_bin)) + num_bin
    print(num_bin)
else:
    print("Il numero di bit inserito non è abbastanza per contenere questo numero!")
