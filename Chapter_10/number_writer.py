<<<<<<< HEAD
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
=======
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
    json.dump(numbers, f)