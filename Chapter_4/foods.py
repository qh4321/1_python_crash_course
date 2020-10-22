my_foods = ['pizza', 'cake', 'ice', 'nuddle']
friend_foods = my_foods[:]

my_foods.append('sushi')
my_foods.append('beef')
my_foods.append('fish')
friend_foods.append('marcon')

print("My favorite foods are： ")
print(my_foods)

print("\nMy friend's favorite foods are: " )
print(friend_foods)

print('\nThe first three items in the list are: ' )
for food in my_foods[0:3]:
  print("-" + food)
print('The items from the middle of the list are: ')
for food in my_foods[2:5]:
  print("-" + food)
print('The last three items in the list are: ')
for food in my_foods[-3:]:
  print("-" + food)
