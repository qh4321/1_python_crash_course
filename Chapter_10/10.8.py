<<<<<<< HEAD
file_names = ['cats.txt', 'dogs.txt', 'bird.txt']

for file_name in file_names:
    print('\nReading ' + file_name)
    try:
        with open(file_name) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        ## pass
        print('Sorry it is not found.')
=======
file_names = ['cats.txt', 'dogs.txt', 'bird.txt']

for file_name in file_names:
    print('\nReading ' + file_name)
    try:
        with open(file_name) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        ## pass
        print('Sorry it is not found.')
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
