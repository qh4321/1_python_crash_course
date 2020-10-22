cars = ['audi', 'bmw', 'benz', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        if car == "benz":
            print(car.upper())
        else:
            print(car.title())


cars = ['audi', 'bmw', 'benz', 'toyota']
for car in cars:
    if car == 'bmw' or car == 'benz':
        print(car.upper())
    else: 
        print(car.title())