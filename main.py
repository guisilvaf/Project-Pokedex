import requests


def pokemon_types(poke):
    print(f'\n{pokemon.capitalize()} type: ')
    for i in poke['types']:
        print(i['type']['name'])


def pokemon_ability(poke):
    print(f'\n{pokemon.capitalize()} abilities: ')
    for i in poke['abilities']:
        print(i['ability']['name'])


def pokemon_moves(poke):
    print(f'\n{pokemon.capitalize()} moves: ')
    for i in poke['moves']:
        print(i['move']['name'])


def pokemon_stats(poke):
    print(f'\n{pokemon.capitalize()} stats: ')
    for i in poke['stats']:
        str(['base_stats'])
        print(i['stat']['name'])


def pokemon_base_stats(poke):
    print(f'\n{pokemon.capitalize()} base stats values: ')
    for i in poke['stats']:
        str(['base_stats'])
        print(i['base_stat'])


def main():
    global pokemon
    pokemon = str(input('Pokemon: '))
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res = requests.get(api)
    poke = res.json()
    pokemon_types(poke)
    pokemon_ability(poke)
    pokemon_moves(poke)
    pokemon_stats(poke)
    pokemon_base_stats(poke)


if __name__ == '__main__':
    main()
