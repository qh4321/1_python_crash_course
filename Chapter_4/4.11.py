my_pizza = ['anana', 'hawaii', 'summer']
friend_pizza = my_pizza[:]

my_pizza.append('fish')
friend_pizza.append('valline')

print('\nMy favorite pizza are:')
for pizza in my_pizza:
    print("-" + pizza)
print("\n friend's favorite pizza are:")
for pizza in friend_pizza:
    print('-' + pizza)