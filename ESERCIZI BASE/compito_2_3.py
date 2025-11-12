# Scrivi un programma in Python che conti quanti sono i quadrati perfetti minori di 200

import math

k = 0

for i in range(200):
    radice = math.sqrt(i)
    if radice % 1 == 0:
        k = k + 1

print(f"Ho contato {k} quadrati perfetti minori di 200")
