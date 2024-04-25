def verificar_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True  # Ano divisível por 400 é bissexto
            else:
                return False  # Ano divisível por 100, mas não por 400, não é bissexto
        else:
            return True  # Ano divisível por 4, mas não por 100, é bissexto
    else:
        return False  # Ano não divisível por 4 não é bissexto

def main():
    ano = int(input("Digite o ano: "))
    if verificar_bissexto(ano):
        print(ano, "é um ano bissexto.")
    else:
        print(ano, "não é um ano bissexto.")

if __name__ == "__main__":
    main()

