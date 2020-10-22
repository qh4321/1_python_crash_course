equation = input("Please enter a equation with two numbers: ")

equation = equation.split()

a = int(equation[0])
b = int(equation[2])
if equation[1] == '+':
    print(a+b)
elif equation[1] == '-':
    print(a-b)
elif equation[1] == '*':
    print(a*b)
elif equation[1] == '/':
    print(a/b)
elif equation[1] == '//':
    print(a//b)
elif equation[1] == '%':
    print(a%b)
else:
    print('Error')

