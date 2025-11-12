def main_0():
    lista_nomi = ["Alice", "Luca", "Giovanni", "Mario"]
    lista_voti = [6, 7, 8, 5]

    # Voglio stampare il voto a fianco di ogni nome
    for nome, voto in zip(lista_nomi, lista_voti):
        print(f"{nome}: {voto}")
        # zip() mi permette di ciclare in parallelo su due o più liste
        # se una lista è più corta si interrompe il for quando finisce la lista più corta


def main():
    lista_nomi = ["Alice", "Luca", "Giovanni", "Mario"]
    lista_voti = [[6, 10, 5],
                  [7, 6],
                  [8, 10, 9, 9],
                  [5, 8]]

    # Modificare il codice sotto per:
    # - stampare la media di ognuno
    # - stampare il numero di voti per ognuno
    # - stampare il voto massimo e minimo di ognuno

    for nome, voti in zip(lista_nomi, lista_voti):
        somma = 0
        for voto in voti:
            somma = somma + voto
        media = somma / len(voti)

        voto_max = 0
        voto_min = 11
        for voto in voti:
            if voto > voto_max:
                voto_max = voto
            if voto < voto_min:
                voto_min = voto

        print(f"{nome}:")
        print(f"- voti: {voti}")
        print(f"- media: {media}")
        print(f"- numero di voti: {len(voti)}")
        print(f"- voto minimo: {voto_min}")
        print(f"- voto massimo: {voto_max}")


if __name__=="__main__":
     main()