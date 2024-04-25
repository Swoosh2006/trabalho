def calcular_perimetro(largura, altura):
    perimetro = 2 * (largura + altura)
    return perimetro

def calcular_area(largura, altura):
    area = largura * altura
    return area

def main():
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

    perimetro = calcular_perimetro(largura, altura)
    area = calcular_area(largura, altura)

    print("O perímetro do retângulo é:", perimetro)
    print("A área do retângulo é:", area)

if __name__ == "__main__":
    main()
