unconfirmed_users = ['alice', 'lidl', 'aldi', 'rewe', 'netto']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)

print('\nThe following users have been confirmed: ')
for user in confirmed_users:
    print(user.title())



## pets

pet = ['dog', 'cat','snake', 'cat', 'dog', 'snake', 'cat', 'cat', 'snake', 'dog' ]
print('\n')
for pe in pet:
    print(pe)

print('\n')
while 'snake' in pet:
    pet.remove('snake')
for pe in pet:
    print(pe)


## mountain_poll

responses = {}

polling = True

while polling:

    name = input('\nWhat is your name? ')
    response = input('Which countain would you like to climb someday? ')

    responses[name] = response

    repeat = input('\nWould you like to let another person response? (yes/no)')
    if repeat == 'no':
        polling = False

print('\n---Result---')
for name, response in responses.items():
    print(name.title() + ' would like to clime the mountain ' + response.title() + '.')
