def main():
    file = open(".\mac-vendors-export.csv", "r", encoding = 'utf-8')
    # risolve i problemi dell apertura file in windows  
    righe = file.readlines()
    file.close()
    #input("Inserisci il mac address-> ")
    mac = "E4:60:17"
    for riga in righe:
        if riga [0:8] == mac:
            print(riga)


if __name__=="__main__":
    main()