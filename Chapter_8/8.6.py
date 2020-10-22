#8.6
def city_country(city, country):
    return city.title() + ' ' + country.title()

city = city_country('santiago', 'chile')
print(city)


#8.7

def make_album(singer, album):
    dic = {'singer': singer.title(),
        'album' : album.title()
        }
    return dic

new = make_album('lala', 'abab')
print(new)

#
def make_album(singer, album, tracks = 0):
    dic = {'singer': singer.title(),
        'album' : album.title()
        }
    if tracks:
        dic['tracks'] = tracks
    return dic

new = make_album('lala', 'abab', tracks = 3)
print(new)


## 8.8

def make_album(singer, album, tracks = 0):
    dic = {'singer': singer.title(),
        'album' : album.title()
        }
    if tracks:
        dic['tracks'] = tracks
    return dic

singer_prompt = "\Which singer do you like? "
album_prompt = "\nWhich album is your favorite? "

print("\nEnter 'quit' to quit at any time.")

while True:
    singer_like = input(singer_prompt)
    if singer_like == 'quit':
        break
    album_like = input(album_prompt)
    if album_like == 'quit':
        break

    new = make_album(singer_like, album_like)
    print(new)
print('\nThank you')


