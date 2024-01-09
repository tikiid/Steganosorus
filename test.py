L = []
for i in range(0, 101, 2):
    if i % 3 == 0:
        L.append(i)
print(L)

L1 = [x for x in range(0,101, 2) if x % 3 == 0]
print(L1)

number_dict = {}

for number in range(0, 100):
    number_dict[f'{number}'] = number
print(number_dict)

animal_name = ["chien", "chat", "lapin", "Éléphant"]
animal_description = ["sympa", "solitaire", "peureux", "trompeur"]
animal_poids = [10, 7, 2.5, 1000]

for name, description, poids in zip(animal_name, animal_description, animal_poids):
    print(name, description, poids)

dict_animal = {name: description for name, description in zip (animal_name, animal_description)}
# voir les sets


# for name, description in zip(animal_name, animal_description):
    # dict_animal[name] = description
print(dict_animal)
'''
etoile = "*"

start = 0
ending = 10

for i in range(start, ending):
    print(" " * (ending-i) + etoile * (i+1))

'''

verify_multiplicity = lambda number, divider : not number % divider


# def verify_multiplicity(number, divider):
    # return not number % divider

list_of_argument = [10, 3]
dict_of_argument = {"number": 10, "divider": 2}

print(verify_multiplicity(*list_of_argument))
print(verify_multiplicity(**dict_of_argument))

# ternaire python 
nombre_maison = 45
print(f"il y a {nombre_maison} maison{'s' if nombre_maison != 1 else "" }")
print(f"il y a {nombre_maison} maison{'s'*bool(nombre_maison-1) }")
print(f"il y a {nombre_maison} maison{'s'*(nombre_maison != 1) }")

# faire du unitest
