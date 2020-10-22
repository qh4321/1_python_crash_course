##
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
}

print('You ordered a  ' + pizza['crust'] + '-crust pizza with the following toppiongs:')

for topping in pizza['toppings']:
    print('\t' + topping)


##
favorite_languages = {
    'Jelly' : ['python', 'r', 'C'],
    'lala' : ['c'],
    'lili' : ['C++', 'java'],
    'phil' : ['lango', 'ruby', 'matlab'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print('\n' + name.title() + "'s favoruite language is:")
    else:
        print('\n' + name.title() + "'s favorite languages are:")
    for language in languages:
        print('\t' +language.title())


## many_users

users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
    },

    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())
