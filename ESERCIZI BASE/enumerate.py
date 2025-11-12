def main_0():
    lista = ["Alice", "Luca", "Giovanni", "Mario"]
    nome_max = None # è il NULL del C
    len_max = 0
    for nome in lista:
        if len(nome) > len_max:
            nome_max = nome
            len_max = len(nome)
    print(nome_max)

def main():
    lista = ["Alice", "Luca", "Giovanni", "Mario"]
    for i, nome in enumerate(lista):
        print(f"{i} - {nome}")


if __name__=="__main__": # dunder (doppio underscore __ )
    print(__name__)
    main()