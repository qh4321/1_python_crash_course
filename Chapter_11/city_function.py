def city_country(city, country, population = ''):
    if population:
        return(city.title() + ',' + country.title() + '-' + population)
    else:
        return(city.title() + ',' + country.title())
