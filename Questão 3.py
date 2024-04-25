def verificar_idade(idade):
    if idade < 13:
        return "Criança"
    elif 13 <= idade <= 17:
        return "Adolescente"
    elif 18 <= idade < 55:
        return "Adulto"
    else:
        return "Idoso"

def main():
    idade = int(input("Digite a idade: "))

    categoria = verificar_idade(idade)

    print("Categoria de idade:", categoria)

if __name__ == "__main__":
    main()
