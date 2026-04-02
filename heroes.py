import requests

url = f"https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)

heroes = response.json()
tallest_heroes = {}

for hero_id in range(len(heroes)):
    gender = heroes[hero_id]['appearance']['gender']
    work = heroes[hero_id]['work']['occupation']
    height = heroes[hero_id]['appearance']['height'][1].split()

    if work == '-':
        work = False
    else:
        work = True

    if height[1] == 'meters':
        height = float(height[0]) * 100
    else:
        height = float(height[0])
    
    key = (gender, work)
    if key not in tallest_heroes:
        tallest_heroes[key] = height
    elif height > tallest_heroes[key]:
        tallest_heroes[key] = height

def get_tallest_hero(gender: str, work: bool) -> str:
    if isinstance(work, bool) == False:
        raise KeyError
    return str(tallest_heroes[(gender, work)]) + " cm"
