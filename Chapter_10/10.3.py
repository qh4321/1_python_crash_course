<<<<<<< HEAD
name = input("What's your name? ")

file_name = 'guest.txt'
with open(file_name, 'w') as file_object:
=======
name = input("What's your name? ")

file_name = 'guest.txt'
with open(file_name, 'w') as file_object:
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
    file_object.write(name.title())