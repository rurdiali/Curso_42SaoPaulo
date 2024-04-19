import sys

def states_capital(city):
    
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }
    
    lista_cidades = list(capital_cities.values())
    lista_estados = list(states.values())
    chaves_cidades = list(capital_cities.keys())
    chaves_estados = list(states.keys())
    
    if city in lista_cidades:
        cidade = chaves_cidades[lista_cidades.index(city)]

        if cidade is not None:
            estados = chaves_estados[lista_estados.index(cidade)]
            print(f"{estados}")
    else:
        print(f"Unknown capital city")
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        states_capital(sys.argv[1])
