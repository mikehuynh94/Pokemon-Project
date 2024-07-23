import requests
import pandas as pd


def get_pokemon() -> dict:
    response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=10300')
    print(response.status_code)
    pokemon_name = response.json()['results']
    df = pd.DataFrame(pokemon_name)
    return df



def find_pokemon(pokemon_id) -> dict:
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    pokemon_id = response.json()['id']
    pokemon_name = response.json()['name']
    pokemon_type = response.json()['types']
    pokemon_abilities = response.json()['abilities']
    pokemon_forms = response.json()['forms']
    pokemon_height = response.json()['height']
    pokemon_stats = response.json()['stats']
    pokemon_moves = response.json()['moves']

    print(f'ID: {pokemon_id}')
    print(f'Name: {pokemon_name}')

    print()
    print('Types:')
    for p_type in pokemon_type:
        print(p_type['type']['name'])

    print()
    print('Abilities:')
    for p_ability in pokemon_abilities:
        print(p_ability['ability']['name'])
        #TO DO get ability effect from https://pokeapi.co/api/v2/ability/

    print()
    print('Forms:')
    for form in pokemon_forms:
        print(form['name'])
    print()
    print(f'Height: {pokemon_height}')
    print()
    print('Stats')
    for stats in pokemon_stats:
        print(stats['stat']['name'], stats['base_stat'])


    pokemon_moves_df = pd.DataFrame(pokemon_moves)
    print()
    print('Moves')
    print(pokemon_moves_df)


print(get_pokemon())

search_id = input('Please enter a pokemon name or id:\n')
if search_id.isdigit() == True:
    find_pokemon(int(search_id))
else:
    find_pokemon(search_id.lower())
