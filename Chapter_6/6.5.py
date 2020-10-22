rivers = {'nile' : 'egypt', 'yangzi' : 'china', 'amazon' : 'brazil'}
for river, country in rivers.items():
    print('\nThe ' + river.title() + 'runs through ' + country.title() + '.')

print('\nThe following rivers are:')
for river in rivers.keys():
    print(river.title())

print('\nThe following countries are:')
for country in rivers.values():
    print(country.title())