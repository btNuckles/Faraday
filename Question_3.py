abc = {
    'animal': 'dog',
    'name': 'Fido',
    'age': 10
    }

output = ('{name} the {animal} is {age} years old'.format(
animal=abc['animal'], name=abc['name'], age=abc['age']))
