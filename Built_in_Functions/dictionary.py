person = {'name': 'Enam', 'age': '20'}

# Accessing person attribute
print(person['name'])  # Prints 'Enam'
print(person['age'])  # Prints '20'

print('------#-------')
# Accessing person attribute using loop
for key in person.keys():
    print(key, '=>', person[key])

# name => Enam
# age => 20
