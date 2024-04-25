def converter_para_conceito(nota):
    if nota >= 9:
        return "A"
    elif nota >= 7.5:
        return "B"
    elif nota >= 6:
        return "C"
    elif nota >= 4:
        return "D"
    else:
        return "F"

def main():
    nota = float(input("Digite a nota: "))

    conceito = converter_para_conceito(nota)

    print("O conceito correspondente à nota {:.2f} é: {}".format(nota, conceito))

if __name__ == "__main__":
    main()