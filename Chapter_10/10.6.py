<<<<<<< HEAD
print('Input two numbers please')
print("Enter 'q' if you are finished.")

while True:
    try:
        first = input("The first number: ")
        if first == 'q':
            break
        x = int(first)
        second = input("The second number: ")
        if second == 'q':
            break
        y = int(second)
    except ValueError:
        print("Sorry it should be a number.")
    else:
        sum = x + y
        print("The sum is " + str(sum))
=======
print('Input two numbers please')
print("Enter 'q' if you are finished.")

while True:
    try:
        first = input("The first number: ")
        if first == 'q':
            break
        x = int(first)
        second = input("The second number: ")
        if second == 'q':
            break
        y = int(second)
    except ValueError:
        print("Sorry it should be a number.")
    else:
        sum = x + y
        print("The sum is " + str(sum))
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
