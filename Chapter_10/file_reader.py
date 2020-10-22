<<<<<<< HEAD
file_path = r'G:\\python_learn\\1_python_crash_course\\chapter_10\\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

##

file_path = r'G:\\python_learn\\1_python_crash_course\\chapter_10\\pi_digits.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

##

file_path = r'G:\\python_learn\\1_python_crash_course\\chapter_10\\pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
=======
file_path = r'G:\\python_learn\\1_python_crash_course\\chapter_10\\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

##

file_path = r'G:\\python_learn\\1_python_crash_course\\chapter_10\\pi_digits.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

##

file_path = r'G:\\python_learn\\1_python_crash_course\\chapter_10\\pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
    print(line.rstrip())