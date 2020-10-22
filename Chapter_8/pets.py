def describe_pet(animal_type , pet_name = 'lady'):
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('hamster', 'harry')
describe_pet('dog')
describe_pet('cat', 'oreo')

describe_pet(pet_name = 'qianjin', animal_type = 'cat')