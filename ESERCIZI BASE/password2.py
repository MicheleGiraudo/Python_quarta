# L'utente inserisce in input una password
# Il programma stampa la password oscurata da * tranne che per la prima lettera

password = input("Inserisci una password: ")
password_blanked = password[0] + "*" * (len(password) - 1)
print(f"Hai inserito la password: {password_blanked}")