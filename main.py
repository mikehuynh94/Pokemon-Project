import requests
import pandas as pd


def get_pokemon() -> dict:
    response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=10300')
    print(response.status_code)
    pokemon_name = response.json()['results']
    df = pd.DataFrame(pokemon_name)
    return df



def find_pokemon(pokemon_id) -> dict:

    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Only try to parse JSON if the content is not empty
        if response.content:
            try:
                pokemon_data = response.json()
                print(f"Pokémon ID: {pokemon_data['id']}")
            except ValueError as json_err:
                print('Invalid response format received from the API. Please try again.', json_err)
        else:
            print('Received empty response from the API. Please try again.')

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print('No Pokémon found with the provided ID or name. Please enter a valid ID or name.')
        else:
            print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as req_err:
        print('An error occurred while trying to fetch data from the API:', str(req_err))
        
    if response.status_code == 200:
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

        print()
        print('Moves')

        # print(f"Name: {pokemon_moves[0]['move']['name']} ({pokemon_moves[0]['move']['url']})")

        # print(pokemon_moves[0]['version_group_details'][0]['level_learned_at'])
        # print(pokemon_moves[0]['version_group_details'][0]['move_learn_method']['name'])
        # print(pokemon_moves[0]['version_group_details'][0]['version_group']['name'])

        for move in pokemon_moves:
            print(f"Name: {move['move']['name']} Url: {move['move']['url']}")
            for move_details in move['version_group_details']:
                print(f"Level learned:{move_details['level_learned_at']}, Method: {move_details['move_learn_method']['name']}, Version group: {move_details['version_group']['name']}")

        # for move in pokemon_moves:
        #   print(move['version_group_details'])
            # if move['version_group_details']['version_group'] == 'emerald':
                # print(move['move'], move['version_group_details'])


# print(get_pokemon())

search_id = input('Please enter a pokemon name or id:\n')
if search_id.isdigit() == True:
    find_pokemon(int(search_id))
else:
    find_pokemon(search_id.lower())
