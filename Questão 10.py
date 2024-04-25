def verificar_numero(numero):
    if numero > 0 and numero % 2 == 0:
        return "Positivo e Par"
    elif numero > 0 and numero % 3 == 0:
        return "Positivo e Múltiplo de Três"
    elif numero < 0 and numero % 2 != 0:
        return "Negativo e Ímpar"
    elif numero == 0:
        return "Zero"
    else:
        return "Nenhum dos casos"

def main():
    numero = int(input("Digite um número: "))
    resultado = verificar_numero(numero)
    print("O número", numero, "é", resultado)

if __name__ == "__main__":
    main()