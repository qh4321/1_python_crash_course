def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

muscian = get_formatted_name('jimi', 'rossmann')
print(muscian)

muscian = get_formatted_name('jimi', 'rossmann', 'lee')
print(muscian)


def build_person(first_name, last_name, age = ' '):
    person = {'first' : first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

muscian = build_person('jimi', 'rossmann', 27)
print(muscian)