## 6.8

pets = []

Oreo = { 
    'name' : "oreo",
    'type' : 'cat',
    'owner' : 'qu',
    'color' : 'black',
}
pets.append(Oreo)

qianjin = {
    'name' : 'qianjin',
    'type' : 'cat',
    'owner' : 'sun',
    'color' : 'brown',
}
pets.append(qianjin)

shiro = {
    'name' : 'shiro',
    'type' : 'dog',
    'owner' : 'xiaoxin',
    'color' : 'white',
}
pets.append(shiro)

for pet in pets:
    print('\nThis is ' + pet['name'].title())
    print(pet)


## 6.9

favorite_places = {
    'Ali' : ['tokyo', 'koln', 'berlin'],
    'Bill' : ['Shanghai', 'Paris', 'amsterdam'],
    'Ayashi' : ['Beijing'],
}

for name, places in favorite_places.items():
    if len(places) == 1:
        print('\n' + name + "'s favorite place is")
    else:
        print('\n' + name + "'s favorite places are")
    for place in places:
        print('\t' + place.title())