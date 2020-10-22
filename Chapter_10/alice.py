<<<<<<< HEAD
file_name = 'alice.txt'

try:
    with open(file_name) as f:
        contents = f.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
=======
file_name = 'alice.txt'

try:
    with open(file_name) as f:
        contents = f.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
    print("The file " + file_name + " has about " + str(num_words) + ' words.')