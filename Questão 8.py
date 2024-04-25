def verificar_triangulo(a, b, c):
    # Verificar se é possível formar um triângulo
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def determinar_tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    a = float(input("Digite o comprimento do lado a: "))
    b = float(input("Digite o comprimento do lado b: "))
    c = float(input("Digite o comprimento do lado c: "))

    if verificar_triangulo(a, b, c):
        tipo_triangulo = determinar_tipo_triangulo(a, b, c)
        print("É possível formar um triângulo.")
        print("O triângulo é", tipo_triangulo)
    else:
        print("Não é possível formar um triângulo com esses comprimentos.")

if __name__ == "__main__":
    main()