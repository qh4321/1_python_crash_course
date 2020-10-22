##8.9 magician

def show_magicians(persons):
    for person in persons:
        print(person.title())

magicians = ['cdac', 'iohji', 'gcudg', 'fuiicd']
show_magicians(magicians)

##8.10

def make_great(persons):
    greats = []
    while persons:
        person = persons.pop()
        g = "The Great " + person.title()
        greats.append(g)
    for great in greats:
        persons.append(great)
    return persons

great_magicians = make_great(magicians[:])
show_magicians(great_magicians)
print(magicians)



    