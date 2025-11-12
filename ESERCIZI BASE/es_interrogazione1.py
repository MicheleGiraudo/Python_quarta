def main():
    file = open(".\es_interrogazione1.csv", "r")
    righe = file.readlines()
    file.close()

    for riga in righe:
        if riga[0] == '#':
            print(riga)

if __name__ == "__main__":
    main()
