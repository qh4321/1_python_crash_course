<<<<<<< HEAD
with open('learning_python') as file_object:
    contents = file_object.read()
    print(contents)


##

with open('learning_python') as file_object:
    for line in file_object:
        print(line)


##

with open('learning_python') as file_object:
    lines = file_object.readlines()

words = ''
for line in lines:
    words += line.strip()

print(words)
=======
with open('learning_python') as file_object:
    contents = file_object.read()
    print(contents)


##

with open('learning_python') as file_object:
    for line in file_object:
        print(line)


##

with open('learning_python') as file_object:
    lines = file_object.readlines()

words = ''
for line in lines:
    words += line.strip()

print(words)
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
print(len(words))