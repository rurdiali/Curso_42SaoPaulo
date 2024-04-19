def transform_to_dict(couples):
    # Cria um dicionário a partir da lista de pares de dicionário
    result_dict = {}
    for name, year in couples:
        result_dict[year] = result_dict.get(year, []) + [name]
    return result_dict

def display_dict(dictionary):
    # Exibe o dicionário na saída padrão no formato especificado
    for year in sorted(dictionary.keys()):
        names = ' '.join(dictionary[year])
        print(f"{year}: {names}")

def main():
    # Lista de pares de dicionário
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]

    # Converte a lista de pares de dicionário em um dicionário
    dictionary = transform_to_dict(d)

    # Exibe o dicionário na saída padrão
    display_dict(dictionary)

if __name__ == "__main__":
    main()

