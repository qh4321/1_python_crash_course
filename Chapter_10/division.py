<<<<<<< HEAD
try:
    print(5/0)
except:
    print("You can't divide by zero!")


##

print("\nGive me two numbers, and I'll divide them. ")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst_number: ")
    if first_number == 'q':
        break
    second_number = input('\nSecond_number: ')
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number)/int(second_number)
        print(answer)
    except ZeroDivisionError:
        print("You can't divide by zero!")
=======
try:
    print(5/0)
except:
    print("You can't divide by zero!")


##

print("\nGive me two numbers, and I'll divide them. ")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst_number: ")
    if first_number == 'q':
        break
    second_number = input('\nSecond_number: ')
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number)/int(second_number)
        print(answer)
    except ZeroDivisionError:
        print("You can't divide by zero!")
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
      