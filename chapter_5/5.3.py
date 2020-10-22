alien_color = 'green'
if alien_color == 'green':
    print("\nYou got 5 points!")


alien_color = 'red'
if alien_color == 'green':
    print('\nYou got 5 points!')
else:
    print('\nYou got 10 points!')


alien_color = 'red'
if alien_color =='green':
    point = 5
elif alien_color == 'yellow':
    point = 10
else:
    point = 15
print('\nYou got ' + str(point) + ' points ！')


fruits = ['banana', 'anana', 'apple', 'watermelon', 'kiwis']
favorite_fruits = ['watermelon', 'peal', 'kiwis']
for fruit in fruits:
    if fruit in favorite_fruits:
        print("\nYou really like " + fruit + " !!")