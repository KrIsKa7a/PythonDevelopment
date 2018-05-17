animal_type = input().lower()

animal_dictionary = {
    "mammal": ["dog"],
    "reptile": ["crocodile", "tortoise", "snake"]
}

animal_class = "unknown"

for key in animal_dictionary.keys():
    values = animal_dictionary[key]

    if animal_type in values:
        animal_class = key

print(animal_class)
