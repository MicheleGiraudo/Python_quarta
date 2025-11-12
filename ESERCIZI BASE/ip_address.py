ip = input("Inserisci un indirizzo IP-> ")
ottetti_str = ip.split(".") # .split(SEP) è un metodo delle stringhe che suddivide una
                            # stringa cercando il carattere separatore SEP
print(ottetti_str)

ottetti= [] # lista vuota
for s in ottetti_str:
    ottetti.append(int(s))

print(ottetti[0])
print(bin(ottetti[0])) #bin ci converte un numero intero in una stringa binaria con prefisso 0b