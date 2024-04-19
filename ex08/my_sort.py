def exibir_musicos_por_ano_e_nome(d):
    # Ordena os músicos pelo ano de nascimento
    sorted_by_year = sorted(d.items(), key=lambda x: x[1])

    # Agrupa os músicos pelo ano de nascimento
    grouped_by_year = {}
    for nome, ano in sorted_by_year:
        grouped_by_year.setdefault(ano, []).append(nome)

    # Exibe os músicos ordenados por ano e depois por nome
    for ano, musicos in grouped_by_year.items():
        print("\nAno:", ano)
        for musico in sorted(musicos):
            print(musico)


d = {
    'Hendrix': '1942',
    'Allman': '1946',
    'Rei': '1925',
    'Clapton': '1945',
    'Johnson': '1911',
    'Baga': '1926',
    'Vaughan': '1954',
    'Cooder': '1947',
    'Página': '1944',
    'Richards': '1943',
    'Hammett': '1962',
    'Cobain': '1967',
    'Garcia': '1942',
    'Beck': '1944',
    'Santana': '1947',
    'Ramone': '1948',
    'Branco': '1975',
    'Frusciante': '1970',
    'Thompson': '1949',
    'Burton': '1939',
}

exibir_musicos_por_ano_e_nome(d)
