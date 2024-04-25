def calcular_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_com_desconto = preco - desconto
    return preco_com_desconto

def main():
    preco = float(input("Digite o preço do produto: R$ "))
    percentual_desconto = float(input("Digite o percentual de desconto (%): "))

    preco_com_desconto = calcular_desconto(preco, percentual_desconto)

    print("Preço com desconto: R$ {:.2f}".format(preco_com_desconto))

if __name__ == "__main__":
    main()