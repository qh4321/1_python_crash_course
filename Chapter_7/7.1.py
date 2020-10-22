## 7.1

car = input("\nWhich car du you want to rent? ")
print('\nLet me see if I can find you a ' + car.title() + '.')


## 7.2

number = input("\nHow many people are in your dinner party tonight? ")
number = int(number)
if number > 8:
    print("\nSorry the table is not avaliable now. ")
else:
    print("\nThe table is ready.")


## 7.3

num = input("\nGive me a number: ")
num = int(num)
if num % 10 == 0:
    print(str(num) + ' is a multiple of 10.')
else:
    print(str(num) + ' is not a multiple of 10.')