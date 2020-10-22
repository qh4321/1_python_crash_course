## 8.12

def sandwich(*toppings):
    print('\nI will make a sandwich with: ')
    for topping in toppings:
        print('  -' + topping)
    print('Your sandwich is ready.')

sandwich('onion', 'beef', 'egg', 'cheese')


## 8.14
def car_info(manufacturer, model, **options):
    car = {}
    car['manufacturer'] = manufacturer.title()
    car['model'] = model.title()
    for key, value in options.items():
        car[key] = value
    return car

car = car_info('subaru', 'outback', color = 'blue', two_package = True)
print(car)

