n = int(input("Quanti numeri di Fibonacci vuoi? ->"))
a, b = 1, 1  #Inizializzazione NON dichiarazione

if n > 2:
    for i in range(n-2):
        a, b = a+b, a+b+b 
        
elif n == 2:
    print()

