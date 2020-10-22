<<<<<<< HEAD
file_name = 'programming reasons'

print("Enter 'quit' if you are finished." )

i =0

while True:
    reason = input('Why do you like programming? ')

    if reason == 'quit':
        break
    else:
        i += 1
        with open(file_name, 'a') as f:
            f.write('Reason ' + str(i) + ': ' + reason + '\n')
        print("You lied！")


=======
file_name = 'programming reasons'

print("Enter 'quit' if you are finished." )

i =0

while True:
    reason = input('Why do you like programming? ')

    if reason == 'quit':
        break
    else:
        i += 1
        with open(file_name, 'a') as f:
            f.write('Reason ' + str(i) + ': ' + reason + '\n')
        print("You lied！")


>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
