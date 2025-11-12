def main():
    file = open("./mac-vendors-export.csv", "r", encoding = 'utf-8')
    righe = file.readlines()
    file.close()

    mac_address = []
    vendor = []

    for riga in righe[1:]: #su [1:] perchè la prima riga e il titolo
        campi = riga.split(",") # per ogni riga ho una lista di campi
        mac_address.append(campi[0])
        vendor.append(campi[1])
    
    mac = input("Inserisci il MAC ddress per intero-> ").upper()
    for m, v in zip(mac_address, vendor):
        if mac[0:8] == m:
            print(f"Il produttore è {v}")

# STAMPARE ANCHE LA DATA DI PRODUZIONE


if __name__=="__main__":
    main()