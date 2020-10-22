prompt = '\nPlease enter your age: '
prompt += "Enter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age != 'quit':
        age = int(age)
        if age < 3:
             print('\nThe cost is free.')
        elif age >= 3 and age < 12:
             print('\nThe cost is $10.')
        else:
             print('\nThe cost is $15.')
    else:
        break