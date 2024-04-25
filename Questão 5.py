def calcular_juros_simples(valor_principal, taxa_juros, periodo):
    juros = valor_principal * (taxa_juros / 100) * periodo
    montante = valor_principal + juros
    return juros, montante

def main():
    valor_principal = float(input("Digite o valor principal: R$ "))
    taxa_juros = float(input("Digite a taxa de juros (em %): "))
    periodo = float(input("Digite o período (em anos): "))

    juros, montante = calcular_juros_simples(valor_principal, taxa_juros, periodo)

    print("O valor dos juros é: R$ {:.2f}".format(juros))
    print("O montante final é: R$ {:.2f}".format(montante))

if __name__ == "__main__":
    main()