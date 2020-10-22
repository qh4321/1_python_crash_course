<<<<<<< HEAD
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
=======
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
    print(line.replace('kl', 'language'))