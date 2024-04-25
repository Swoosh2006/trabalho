def converter_unidades(valor, unidade_origem):
    # Dicionário com fatores de conversão para cada unidade
    fatores = {
        'milhas': {'milhas': 1, 'polegadas': 63360, 'pés': 5280, 'centímetros': 160934, 'metros': 1609.34, 'quilômetros': 1.60934},
        'polegadas': {'milhas': 1/63360, 'polegadas': 1, 'pés': 1/12, 'centímetros': 2.54, 'metros': 0.0254, 'quilômetros': 0.0000254},
        'pés': {'milhas': 1/5280, 'polegadas': 12, 'pés': 1, 'centímetros': 30.48, 'metros': 0.3048, 'quilômetros': 0.0003048},
        'centímetros': {'milhas': 1/160934, 'polegadas': 1/2.54, 'pés': 1/30.48, 'centímetros': 1, 'metros': 0.01, 'quilômetros': 0.00001},
        'metros': {'milhas': 1/1609.34, 'polegadas': 1/0.0254, 'pés': 1/0.3048, 'centímetros': 100, 'metros': 1, 'quilômetros': 0.001},
        'quilômetros': {'milhas': 1/1.60934, 'polegadas': 1/0.0000254, 'pés': 1/0.0003048, 'centímetros': 100000, 'metros': 1000, 'quilômetros': 1}
    }
    
    # Obtendo as unidades de destino
    unidades_destino = [unidade for unidade in fatores[unidade_origem].keys() if unidade != unidade_origem]
    
    # Convertendo para todas as unidades de destino
    valores_convertidos = {}
    for unidade in unidades_destino:
        valor_convertido = valor * fatores[unidade_origem][unidade]
        valores_convertidos[unidade] = valor_convertido
    
    return valores_convertidos

def main():
    valor = float(input("Digite o valor a ser convertido: "))
    unidade_origem = input("Digite a unidade de medida de origem (milhas, polegadas, pés, centímetros, metros ou quilômetros): ").lower()

    if unidade_origem not in ['milhas', 'polegadas', 'pés', 'centímetros', 'metros', 'quilômetros']:
        print("Unidade de medida inválida.")
        return

    resultados = converter_unidades(valor, unidade_origem)

    print(f"\n{valor} {unidade_origem} equivalem a:")
    for unidade, valor_convertido in resultados.items():
        print(f"{valor_convertido:.2f} {unidade}")

if __name__ == "__main__":
    main()