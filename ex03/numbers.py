def ler_numeros_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            numeros = arquivo.read().split(',')
            return [int(numero.strip()) for numero in numeros]
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []

def exibir_numeros(numeros):
    for numero in numeros:
        print(numero)

def main():
    nome_arquivo = 'numbers.txt'  # Caminho para o arquivo numbers.txt
    numeros = ler_numeros_arquivo(nome_arquivo)
    exibir_numeros(numeros)

if __name__ == "__main__":
    main()
