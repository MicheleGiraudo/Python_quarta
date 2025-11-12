# il carattere # serve per i commenti.
# In questo programma useremo l'assegnazione.
# In python non ci sono dichiarazioni, Python fa
# dynamic tipe checking (controllo dinamico dei tipi)
# sulla base dei valori assegnati dalle variabili

a = input("Scrivi qualcosa -->")    #"input" permette di chiedere in input qualcosa da digitare all'utente
# "input" restituisce SEMPRE stringhe!!
# Facciamo una print con una f-string ---> la f ti permette di inserire le variabili nelle print
print(f"Hai inserito {a} che è di tipo {type(a)}")