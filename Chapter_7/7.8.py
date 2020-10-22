## 7.8

sandwich_orders = ['anana sandwich', 'tuna sandwich', 'vegi sandwich', 'beef sandwich']
finished_sandwich = []

while sandwich_orders:
    cocking_sandwich = sandwich_orders.pop()
    print('\nI made your ' + cocking_sandwich)
    finished_sandwich.append(cocking_sandwich)

print("\nI have made these sandwiches: ")
for sandwich in finished_sandwich:
    print('\t-' + sandwich)


## 7.9

sandwich_orders = ['anana sandwich','pastrami sandwich', 'tuna sandwich','pastrami sandwich', 'vegi sandwich','pastrami sandwich', 'beef sandwich']
finished_sandwich = []

print('\nSorry pastrami sandwich is sold out.')

while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

while sandwich_orders:
    cocking_sandwich = sandwich_orders.pop()
    print('\nI made your ' + cocking_sandwich)
    finished_sandwich.append(cocking_sandwich)

print("\nI have made these sandwiches: ")
for sandwich in finished_sandwich:
    print('\t-' + sandwich)


## 7.9
responses = {}

polling = True

while polling:
    name = input("\nWhat's your name? ")
    response = input("\nIf you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person response?(yes/no) ")
    if repeat == 'no':
        polling = False

print("\n---Result---")
for name, response in responses.items():
    print(name.title() + ' wants to visit ' + response.title() + '.')