#FIBONACCI
# Primo giro: a = 1 --- b = 1
# Secondo giro: a = a + b --- b = a + b

n = int(input("quanti numeri di fibonacci vuoi? ->"))
a, b = 1, 1

if n > 2:
    for i in range(n):
        print(a, end =" - ")
        a,b = b,a+b

elif n == 0:
    print("Nessun numero stampato.")

elif n == 2:
    print(a, end = " - ")
    print(b)

elif n == 1:
    print(a)

