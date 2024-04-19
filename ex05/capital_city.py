def find_capital(state):
    # Dicionários com os estados e suas abreviações e as capitais
    estados = {
        "Oregon": "OU",
        "Alabama": "AL",
        "Nova Jersey": "NJ",
        "Colorado": "CO"
    }
    cidades_capital = {
        "OU": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    # Verifica se o estado fornecido está no dicionário de estados
    if state in estados:
        # Encontra a abreviação do estado
        abreviacao = estados[state]
        # Verifica se a abreviação está no dicionário de capitais
        if abreviacao in cidades_capital:
            # Exibe a capital correspondente ao estado
            print(cidades_capital[abreviacao])
        else:
            print("Capital desconhecida")
    else:
        print("Estado desconhecido")

def main():
    import sys
    # Verifica se foi fornecido um argumento na linha de comando
    if len(sys.argv) != 2:
        # Se nenhum argumento foi fornecido, ou muitos foram fornecidos, o programa não faz nada e sai
        return
    # Obtém o estado fornecido como argumento
    state = sys.argv[1]
    # Chama a função para encontrar a capital correspondente ao estado
    find_capital(state)

if __name__ == "__main__":
    main()

