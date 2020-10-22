<<<<<<< HEAD
def count_words(file_name):
    try:
        with open(file_name) as f:
            contents = f.read()
    except FileNotFoundError:
            ##pass
            msg = "\nSorry, the file " + file_name + " can not be founded."
            print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("\nThe file " + file_name + " has about " + str(num_words) + " words.")

file_names = ['alice.txt', 'sidhartha.txt', 'moby_dict.txt', 'little_women.txt']
for file_name in file_names:
=======
def count_words(file_name):
    try:
        with open(file_name) as f:
            contents = f.read()
    except FileNotFoundError:
            ##pass
            msg = "\nSorry, the file " + file_name + " can not be founded."
            print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("\nThe file " + file_name + " has about " + str(num_words) + " words.")

file_names = ['alice.txt', 'sidhartha.txt', 'moby_dict.txt', 'little_women.txt']
for file_name in file_names:
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
    count_words(file_name)