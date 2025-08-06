people = [
    {"name": "Giorgi", "age": 20},
    {"name": "Mariam", "age": 16},
    {"name": "Nika", "age": 25}
]

print("People older than 18:")
for person in people:
    if person["age"] > 18:
        print(person)