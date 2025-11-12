# In Python possiamo delimitare con "..." oppure con '...'
stringa = "Ciao mondo!"
print(stringa)

# Esempio di INDICIZZAZIONE della stringa
# Indicizzare significa estrarre un carattere da una stringa
print(f"L'ultimo carattere della stringa è {stringa[-1]}")

# Esempio di SLICING delle stringhe 
print(f"La sottostringa 2-6 è {stringa[2:6]}.")
# Prende tutti i caratteri presenti tra l'indice di sinistra incluso e l'indice di destra escluso

#ASSEGNAZIONE MULTIPLA ---> va bene con qualsiasi tipo di dato
nome, cognome = "Mario", "Rossi"
# oppure 
# nome = "Mario"
# cognome = "Rossi"

# CONCATENAZIONE
# Concateno la stringa nome e la stringa cognome, x è una stringa, " " è per ottenere uno spazio
x = nome + " " + cognome 
print(x)  

#CONCATENAZIONE MULTIPLA
y = nome*5
print(y)

