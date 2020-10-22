<<<<<<< HEAD
import json

try:
    with open('favorite_number.json') as f:
        num = json.load(f)

except FileNotFoundError:
    num = input("What's your favorite number? ")
    with open('favorite_number.json', 'w') as f:
           json.dump(num, f)
    print("I'll remember it. ")

else:
    print("I know your favorite number is " + str(num) + '.')
=======
import json

try:
    with open('favorite_number.json') as f:
        num = json.load(f)

except FileNotFoundError:
    num = input("What's your favorite number? ")
    with open('favorite_number.json', 'w') as f:
           json.dump(num, f)
    print("I'll remember it. ")

else:
    print("I know your favorite number is " + str(num) + '.')
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
