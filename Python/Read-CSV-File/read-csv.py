from csv import DictReader

VACCINES_NAMES = [
    'Canine Parvo',
    'Canine Distemper',
    'Canine Rabies',
    'Canine Leptospira',
    'Feline Herpes Virus 1',
    'Feline Rabies',
    'Feline Leukemia'
]
print(DictReader(open('./pet_data.csv')))


class Pet:
    name = ''
    age = 0
    description = ''
    submitter = ''
    species = ''
    breed = ''
    sex = ''


pet_arr = []
for row in DictReader(open('./pet_data.csv')):
    pet = Pet()
    pet.name = row['Pet']
    pet.age = row['Pet']
    pet.name = row['Pet']
    pet.name = row['Pet']
    pet.name = row['Pet']
    pet.name = row['Pet']
    pet.name = row['Pet']
    pet_arr.append(pet)

print(pet_arr[0])
