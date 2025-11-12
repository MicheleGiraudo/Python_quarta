# Ci sono tanti modi di fare il for i python
# Vediamo il primo modo, detto C-style

for i in range(4):   # Corre da 0 a 4 escluso
    print(i)

for i in range(1,4):
    print(i)

#range(START, STOP, GAP)  --> start e gap parametri facoltativi
#quindi si scrivono così nella documentazione: range([START], STOP, [GAP])
for i in range(8, 1, -2):
    print(i)