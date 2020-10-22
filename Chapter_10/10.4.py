<<<<<<< HEAD
file_name = "guest_book.txt"

print("Enter 'quit' if you are finished.")
i = 0
while True:
    name = input("Hi what's your name baby. ")
    if name == 'quit':
        break
    else:
        i += 1
        with open(file_name, 'a') as f:
            f.write('No' + str(i) +': '+ name.title() + '\n')
=======
file_name = "guest_book.txt"

print("Enter 'quit' if you are finished.")
i = 0
while True:
    name = input("Hi what's your name baby. ")
    if name == 'quit':
        break
    else:
        i += 1
        with open(file_name, 'a') as f:
            f.write('No' + str(i) +': '+ name.title() + '\n')
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
        print("Your name has been added baby. ")