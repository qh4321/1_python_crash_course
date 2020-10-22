alien_0 = { 'color' : 'green', 'points' : 5}

print(alien_0['color'])
print(alien_0['points'])

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


alien_1 = {}

alien_1['color'] = 'yellow'
alien_1['points'] = 10
print(alien_1)

print('\nThe alien is ' + alien_0['color'] + '.')
alien_0['color'] = 'red'
print('\nThe alien is now ' + alien_0['color'] +'.')

#6.2.4

alien_0 = {'x_position':0, 'y_position' :25, 'speed':'medium'}
print("\nOriginal x-position: " + str(alien_0['x_position']))
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print('\nNew x-position: ' + str(alien_0['x_position']))