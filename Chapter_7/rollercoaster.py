## rollercoaster
height = input("\n15How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print('\nYou are tall enough to ride!')
else:
    print("\nYou'll be able to ride when you're a little older.")


## even_or_odd

number = input("Enter a number ")
number = int(number)

if number %2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")