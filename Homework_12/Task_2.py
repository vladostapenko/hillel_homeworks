import requests
import json


def get_starship_info():
    # Виконання запиту до API для отримання інформації про корабель Millennium Falcon
    response = requests.get('https://swapi.dev/api/starships/10/')
    starship_data = response.json()

    # Інфо про пілотів
    pilots_info = []
    for pilot_url in starship_data['pilots']:
        pilot_response = requests.get(pilot_url)
        pilot_data = pilot_response.json()
        pilot_info = {
            'name': pilot_data['name'],
            'height': pilot_data['height'],
            'mass': pilot_data['mass'],
            'homeworld': pilot_data['homeworld'],
            'homeworld_info': get_homeworld_info(pilot_data['homeworld'])
        }
        pilots_info.append(pilot_info)

    # Створя дікту з інфо про корабель та пілотів
    starship_info = {
        'name': starship_data['name'],
        'max_speed': starship_data['max_atmosphering_speed'],
        'class': starship_data['starship_class'],
        'pilots': pilots_info
    }

    return starship_info


def get_homeworld_info(homeworld_url):
    # Отримання інфо про планету пілота
    response = requests.get(homeworld_url)
    homeworld_data = response.json()
    return {
        'name': homeworld_data['name'],
        'climate': homeworld_data['climate'],
        'terrain': homeworld_data['terrain']
    }


def save_to_json(data, filename):
    # Збереження данних в JSON
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    starship_info = get_starship_info()
    print(starship_info)
    save_to_json(starship_info, 'starship_info.json')
