# Serialize and Deserialize
import json
people = [
    {'name': 'Alice', 'age':23, 'score':88},
    {'name': 'Kings', 'age':95}
]

with open('people.json', 'w', encoding='utf-8') as f:
    json.dump(people, f, indent=2)
print('Wrote people.json')

with open('people.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print('\nLoaded JSON:', data)
