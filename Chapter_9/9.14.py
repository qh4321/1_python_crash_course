from random import randint

class Die():
    
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


d6 = Die()

results = []

for num in range(1,11):
    result = d6.roll_die()
    results.append(result)
print('\n10 times rolls of a 6 sides die:')
print(results)


d10 = Die(10)

results = []

for num in range(1,11):
    result = d10.roll_die()
    results.append(result)
print('\n10 times rolls of a 10 sides die:')
print(results)


d20 = Die(sides = 20)

results = []

for num in range(1,11):
    result = d20.roll_die()
    results.append(result)
print('\n10 times rolls of a 20 sides die:')
print(results)

